# LLM RAG-Powered CI/CD Failure Analysis Agent

> **Intelligent Root Cause Analysis & Remediation for CI/CD Pipeline Failures**

A sophisticated multi-step LangChain agent that ingests CI/CD failure logs, performs automated Root Cause Analysis (RCA) via LLM reasoning, and surfaces structured remediation suggestions to dramatically reduce time-to-diagnosis in test pipelines.

## 🎯 Project Overview

This system combines **Large Language Models (LLMs)**, **Retrieval-Augmented Generation (RAG)**, and **intelligent agent orchestration** to provide automated, context-aware analysis of CI/CD pipeline failures.

### Key Capabilities

- **🔍 Intelligent RCA**: Automatically identifies root causes from CI/CD failure logs using GPT-4-turbo reasoning
- **📚 Knowledge-Aware Analysis**: Integrates internal documentation through ChromaDB RAG for context-aware diagnosis
- **💡 Actionable Remediation**: Generates prioritized, step-by-step remediation suggestions with success probability estimates
- **⚡ Reduced Time-to-Diagnosis**: From hours of manual investigation to seconds of automated analysis
- **🔐 Structured Output**: JSON-formatted results suitable for integration with monitoring and ticketing systems

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    CI/CD Failure Logs                        │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │   Log Parser & Processor     │
        │  (Parse, validate, extract)  │
        └──────────┬───────────────────┘
                   │
        ┌──────────┴──────────────────────────────┐
        ▼                                         ▼
┌──────────────────┐                  ┌──────────────────────┐
│  RAG Pipeline    │◄─────────────────►│ ChromaDB Vector DB   │
│ (Document Retriev)                  │ (Documentation Index)│
└──────────────────┘                  └──────────────────────┘
        │
        ▼
┌──────────────────────────────────────────────────────────────┐
│               LangChain Agent Orchestrator                    │
├──────────────────────────────────────────────────────────────┤
│  ┌──────────────────────┐      ┌───────────────────────────┐ │
│  │   RCA Agent          │      │  Remediation Agent        │ │
│  │  (Root Cause Analysis)      │  (Suggest Fixes)          │ │
│  └──────────┬───────────┘      └────────────┬──────────────┘ │
│             │                               │                │
│             └───────────┬────────────────────┘                │
│                         │                                     │
│             ┌───────────▼──────────────────┐                 │
│             │  GPT-4-Turbo LLM             │                 │
│             │  (Reasoning & Generation)    │                 │
│             └──────────────────────────────┘                 │
└──────────────────────────────────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────────────────────────────┐
│              Structured Results (JSON)                        │
├──────────────────────────────────────────────────────────────┤
│ • Root Causes                                                │
│ • Failure Chain Analysis                                     │
│ • Affected Components                                        │
│ • Severity & Confidence Score                                │
│ • Prioritized Remediation Steps                              │
│ • Success Probability Estimates                              │
└──────────────────────────────────────────────────────────────┘
```

## 📊 Data Definitions

### Log Entry Structure

```python
@dataclass
class LogEntry:
    timestamp: datetime          # When the event occurred
    level: LogLevel             # ERROR, WARNING, INFO, DEBUG
    component: str              # What component produced the log
    message: str                # The log message
    stack_trace: Optional[str]  # Full error stack trace if available
    raw_log: Optional[str]      # Raw log line for reference
```

### RCA Analysis Output

```json
{
  "root_causes": [
    "Database connection pool exhausted",
    "Timeout configuration set too low"
  ],
  "failure_chain": [
    "High concurrent request load",
    "Connection acquisition delayed",
    "Timeout reached before connection acquired",
    "Test marked as failed"
  ],
  "affected_components": [
    "database_service",
    "api_client",
    "test_runner"
  ],
  "severity": "HIGH",
  "impact": "45% of test suite fails intermittently",
  "confidence_score": 0.87,
  "summary": "Connection pool exhaustion due to long-running queries..."
}
```

### Remediation Suggestion Format

```json
{
  "action": "Increase database connection pool size",
  "priority": "HIGH",
  "estimated_fix_time": "15 minutes",
  "risk_level": "LOW",
  "success_probability": 0.92,
  "steps": [
    "Update DB_POOL_SIZE environment variable from 10 to 20",
    "Restart the API service with new configuration",
    "Monitor connection metrics for 5 minutes",
    "Re-run test suite to verify fix"
  ],
  "details": "The connection pool is being exhausted...",
  "related_docs": [
    "connection_pool_guide.md",
    "performance_benchmarks.md"
  ]
}
```

## 🛠️ Components

### 1. **LangChain Agents** (`src/agents/`)

#### RCAAgent
- Analyzes failure logs using LLM reasoning
- Identifies root causes and failure chains
- Provides confidence scores and severity assessment
- Integrates with RAG for contextual documentation

#### RemediationAgent
- Generates actionable fix suggestions
- Prioritizes recommendations by impact
- Estimates time-to-fix and success probability
- Links suggestions to relevant documentation

#### CIDDQAAgent
- Orchestrates the complete analysis workflow
- Coordinates RCA and Remediation agents
- Returns comprehensive results with metadata

### 2. **RAG System** (`src/rag/`)

#### ChromaDBManager
- Manages ChromaDB vector database operations
- Handles document ingestion and retrieval
- Provides collection statistics

#### DocumentProcessor
- Chunks documentation files for optimal retrieval
- Supports configurable chunk size and overlap
- Handles multiple file formats

#### RAGPipeline
- Complete end-to-end RAG workflow
- Ingests documentation from multiple sources
- Performs semantic search over documentation

### 3. **Utilities** (`src/utils/`)

#### Parser (`parser.py`)
- Parses CI/CD logs (JSON and text formats)
- Extracts error context and stack traces
- Supports multiple log format variations

#### Logger (`logger.py`)
- Structured logging with loguru
- File and console output
- Configurable log levels

#### Formatter (`formatter.py`)
- Formats RCA analysis for human consumption
- Decorates remediation suggestions with priorities
- Converts results to JSON, Markdown, etc.

## 🚀 Getting Started

### Prerequisites

- **Python 3.10 or higher** - [Download here](https://www.python.org/downloads/)
- **OpenAI API key** - [Get one free here](https://platform.openai.com/account/api-keys)
- **Git** - For cloning the repository
- **Any OS**: Windows, macOS, or Linux

### Step 1: Get Your OpenAI API Key

1. Visit [OpenAI API Keys](https://platform.openai.com/account/api-keys)
2. Sign up or log in (credit card required for paid usage)
3. Click **"Create new secret key"**
4. Copy the key (it will only be shown once)
5. Store it safely - you'll need it in Step 4

### Step 2: Clone & Setup Project

#### Windows (PowerShell)
```powershell
# Clone the repository
git clone https://github.com/yourusername/llm_rag_powered_qa_agent.git
cd llm_rag_powered_qa_agent

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

#### macOS/Linux (Bash)
```bash
# Clone the repository
git clone https://github.com/yourusername/llm_rag_powered_qa_agent.git
cd llm_rag_powered_qa_agent

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Configure Environment

#### Option A: Create `.env` File (Recommended)

Create a `.env` file in the project root:

```bash
# .env file
OPENAI_API_KEY=sk-YOUR_API_KEY_HERE

# Optional: Customize settings (defaults shown)
LLM_MODEL=gpt-3.5-turbo
TEMPERATURE=0.7
CHROMA_DB_PATH=./chroma_db
LOG_LEVEL=INFO
```

#### Option B: Set Environment Variables

**Windows (PowerShell)**:
```powershell
$env:OPENAI_API_KEY = "sk-YOUR_API_KEY_HERE"
```

**macOS/Linux (Bash)**:
```bash
export OPENAI_API_KEY="sk-YOUR_API_KEY_HERE"
```

### Step 4: Ingest Documentation (First Time Only)

The system needs documentation to provide context-aware analysis. Prepare your docs first:

```powershell
# Windows
python examples/ingest_docs.py

# macOS/Linux
python examples/ingest_docs.py
```

This ingests the sample documentation from `data/documentation/`. For **custom documentation**:

1. Add Markdown files to `data/documentation/`
2. Run the ingestion script again
3. Files are automatically parsed and added to ChromaDB

### Step 5: Verify Installation

```powershell
# Run the test suite
.\run-tests.ps1

# Should see: [PASS] All tests passed!
```

### Basic Usage

**Minimal Example:**
```python
from src.agents import CIDDQAAgent

# Initialize (automatically loads ChromaDB docs)
agent = CIDDQAAgent()

# Read your CI/CD failure logs
with open("failure.log", "r") as f:
    log_content = f.read()

# Analyze
result = agent.analyze_and_remediate(log_content)

# Access results
print(f"Root Causes: {result['rca']['root_causes']}")
print(f"Severity: {result['rca']['severity']}")
for suggestion in result['remediation_suggestions']:
    print(f"- {suggestion['action']}")
```

**Complete Example:**
```python
import json
from src.agents import CIDDQAAgent
from src.rag import RAGPipeline

# Initialize with custom RAG pipeline
rag_pipeline = RAGPipeline()

# Ingest additional documentation
rag_pipeline.ingest_documentation([
    "data/documentation/my_guide.md"
])

# Create agent with the RAG pipeline
agent = CIDDQAAgent(rag_pipeline)

# Load and analyze logs
with open("failure.log", "r") as f:
    log_content = f.read()

# Run analysis
result = agent.analyze_and_remediate(log_content, query="Database timeout")

# Pretty print results
print(json.dumps(result, indent=2, default=str))
```

## 📖 Running Examples

### Example 1: Analyze a CI/CD Failure

```bash
# Method 1: Run the provided example
python examples/analyze_failure.py

# Method 2: Use the test logs directly
```

### Example 2: Ingest Custom Documentation

```powershell
# 1. Add your documentation files
Copy-Item "my_docs/*.md" -Destination "data/documentation/"

# 2. Ingest them
python examples/ingest_docs.py

# 3. Verify ingestion
# Check data/logs/ for ingestion logs
```

### Example 3: Use the FastAPI Server

```powershell
# Start the API server
python examples/api_server.py

# The server will start on http://localhost:8000
# API docs: http://localhost:8000/docs

# Test the API with curl (Windows PowerShell)
$logContent = Get-Content "failure.log" -Raw
$body = @{
    log_content = $logContent
    query = "database timeout"
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:8000/analyze" `
    -Method POST `
    -Headers @{"Content-Type"="application/json"} `
    -Body $body
```

### Example 4: Batch Analysis

```python
# Analyze multiple failure logs
from pathlib import Path
from src.agents import CIDDQAAgent

agent = CIDDQAAgent()
results = {}

for log_file in Path("data/logs").glob("*.log"):
    with open(log_file) as f:
        analysis = agent.analyze_and_remediate(f.read())
        results[log_file.name] = analysis

# Export results
import json
with open("batch_analysis_results.json", "w") as f:
    json.dump(results, f, indent=2, default=str)
```

## 🐳 Docker Deployment

### Option A: Desktop Testing

```bash
# Build the image
docker build -t rag-qa-agent .

# Run with environment variable
docker run -e OPENAI_API_KEY="sk-..." rag-qa-agent

# Or with .env file
docker run --env-file .env rag-qa-agent
```

### Option B: Production Deployment (docker-compose)

```bash
# Start the service
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the service
docker-compose down
```

**docker-compose.yml** includes:
- Main Python service with RAG + agents
- Persistent ChromaDB volume
- Environment variable configuration
- Health checks

## ⚙️ Configuration Reference

### Environment Variables

Create a `.env` file or set these in your shell:

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENAI_API_KEY` | *(required)* | Your OpenAI API key (sk-...) |
| `LLM_MODEL` | `gpt-3.5-turbo` | Which GPT model to use |
| `TEMPERATURE` | `0.7` | LLM creativity (0=precise, 1=creative) |
| `MAX_TOKENS` | `2000` | Max response length |
| `CHROMA_DB_PATH` | `./chroma_db` | Where to store vector DB |
| `CHROMA_COLLECTION_NAME` | `ci_cd_docs` | Vector DB collection name |
| `CHUNK_SIZE` | `1000` | Document chunk size |
| `CHUNK_OVERLAP` | `200` | Overlap between chunks |
| `TOP_K_RETRIEVAL` | `3` | Docs to retrieve per query |
| `LOG_LEVEL` | `INFO` | Logging verbosity |

### Performance Tuning

**For Faster Analysis:**
```bash
CHUNK_SIZE=2000          # Fewer but larger chunks
TOP_K_RETRIEVAL=1        # Retrieve fewer docs
TEMPERATURE=0.3          # More deterministic
```

**For Better Context:**
```bash
CHUNK_SIZE=500           # More smaller chunks
TOP_K_RETRIEVAL=5        # Retrieve more docs
TEMPERATURE=0.9          # More creative analysis
```

## 🛠️ Troubleshooting

### Issue: "OPENAI_API_KEY not found"

**Solution:**
```powershell
# Verify the key is set
$env:OPENAI_API_KEY

# If empty, set it
$env:OPENAI_API_KEY = "sk-..."

# For permanent setup, edit or create .env file
# OPENAI_API_KEY=sk-...
```

### Issue: "ModuleNotFoundError: No module named 'langchain'"

**Solution:**
```powershell
# Ensure virtual environment is activated
venv\Scripts\Activate.ps1

# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### Issue: "ChromaDB collection is empty"

**Solution:**
```powershell
# Ingest the documentation first
python examples/ingest_docs.py

# Verify documents were added
python -c "from src.rag import RAGPipeline; print(RAGPipeline().get_stats())"
```

### Issue: "OPENAI_API_KEY invalid or expired"

**Solution:**
1. Check your API key is correct: Copy-paste from [OpenAI dashboard](https://platform.openai.com/account/api-keys)
2. Verify key has billing enabled (free trial may have expired)
3. Check usage limits: https://platform.openai.com/account/billing/usage
4. Generate a new key if needed

### Issue: "Connection took too long" or "Timeout"

**Solution:**
```bash
# Likely hitting OpenAI rate limits or network issues
# Try again after a few seconds, or reduce request frequency
```

### Issue: "Vector database corrupted or out of space"

**Solution:**
```powershell
# Delete and recreate ChromaDB
Remove-Item -Recurse -Force chroma_db/

# Re-ingest documentation
python examples/ingest_docs.py
```

## 📊 Monitoring & Debugging

### Enable Verbose Logging

```powershell
# Set environment variable
$env:LOG_LEVEL = "DEBUG"

# Run your analysis - you'll see detailed logs
```

### Check RAG System Health

```python
from src.rag import RAGPipeline

rag = RAGPipeline()
stats = rag.get_stats()

print(f"Database: {stats['collection_name']}")
print(f"Documents: {stats['document_count']}")
print(f"Ready: {stats['document_count'] > 0}")
```

### View ChromaDB Contents

```python
from src.rag import ChromaDBManager

db = ChromaDBManager()
# Query to see what's stored
results = db.query("database connection")
print(f"Found {len(results['documents'][0])} matching docs")
```

## 🧠 AI Tools & Models

### Large Language Model
- **Model**: GPT-4-Turbo
- **Provider**: OpenAI
- **Purpose**: Complex reasoning for RCA and remediation generation
- **Configuration**:
  - Temperature: 0.7 (for balanced creativity and consistency)
  - Max Tokens: 2000 (sufficient for detailed analysis)
  - Top-p sampling: Default

### Embedding Model
- **Model**: OpenAI Embeddings (via ChromaDB)
- **Purpose**: Semantic search over documentation
- **Dimension**: 1536
- **Distance Metric**: Cosine similarity

### Vector Database
- **System**: ChromaDB
- **Type**: Open-source vector database
- **Purpose**: Persistent storage and retrieval of document embeddings
- **Features**: Built-in embedding, fast similarity search, metadata filtering

## 💾 Infrastructure & Storage

### Vector Database (ChromaDB)

**Default Setup (Local Development):**
- **Type**: Vector Database with file-based persistence
- **Location**: `./chroma_db/` directory
- **Capacity**: Up to 100K documents
- **No setup required**: Automatically created on first use

**Production Setup (Elastic Search):**
Example Elasticsearch configuration:
```yaml
# docker-compose.yml addition
elasticsearch:
  image: docker.elastic.co/elasticsearch/elasticsearch:8.0.0
  environment:
    discovery.type: single-node
  ports:
    - "9200:9200"
```

### Storage Recommendations

| Use Case | Storage | Size | Durability |
|----------|---------|------|-----------|
| **Development** | Local disk | < 1GB | Backup monthly |
| **Staging** | Cloud storage (S3) | 1-10GB | Daily snapshots |
| **Production** | Managed DB (Atlas) | 10GB+ | Real-time replication |

### Backup Strategy

```powershell
# Backup ChromaDB
Copy-Item -Recurse "chroma_db" "chroma_db_backup_$(Get-Date -Format 'yyyyMMdd')"

# Or use docker volumes for automatic backups
# docker run -v chroma_db_volume:/app/chroma_db ...
```

## 🚀 Deployment Options

### Option 1: Standalone Python Script (Simplest)

**For**: Small teams, one-off analysis, testing

```powershell
# Requirements
python requirements.txt
OPENAI_API_KEY set

# Run
python examples/analyze_failure.py
```

### Option 2: FastAPI Server (Recommended)

**For**: Team access, integration with monitoring, REST API

```powershell
# Start server
python examples/api_server.py

# Access at http://localhost:8000
# API docs at http://localhost:8000/docs
```

### Option 3: Docker Container

**For**: Consistent environments, cloud deployment

```bash
# Build
docker build -t ci-cd-analyzer .

# Run
docker run -e OPENAI_API_KEY="sk-..." ci-cd-analyzer
```

### Option 4: Kubernetes/Cloud (Enterprise)

**For**: Large scale, high availability

```yaml
# Example: Google Cloud Run
apiVersion: run.cnpg.io/v1alpha1
kind: Run
metadata:
  name: rag-qa-agent
spec:
  image: gcr.io/myproject/rag-qa-agent:latest
  environmentSecrets:
    - OPENAI_API_KEY  # Use Cloud Secret Manager
  memory: 1Gi
  cpu: 2
```

## 📈 Performance & Optimization

### Typical Performance Metrics

| Operation | Time | Notes |
|-----------|------|-------|
| First-time setup | 2 min | Includes ChromaDB init |
| Document ingestion | 5-15s per file | Depends on file size |
| Single log analysis | 8-15s | Including LLM response |
| RAG query | 100-300ms | Vector similarity search |
| LLM inference | 3-10s | OpenAI API latency |

### Optimization Tips

**Speed Up Document Retrieval:**
```bash
TOP_K_RETRIEVAL=1        # Return fewer docs (faster but less context)
CHUNK_SIZE=2000          # Larger chunks (fewer to process)
```

**Improve Analysis Quality:**
```bash
TOP_K_RETRIEVAL=5        # Return more docs (better context)
CHUNK_SIZE=500           # Smaller chunks (more precise)
TEMPERATURE=0.5          # More deterministic
```

**Reduce OpenAI Costs:**
```bash
LLM_MODEL=gpt-3.5-turbo  # Cheaper alternative (may be less accurate)
MAX_TOKENS=1000          # Limit response length
```

### Caching Strategy

```python
# Cache results for similar failures
import json
from pathlib import Path

cache_dir = Path("analysis_cache")
cache_dir.mkdir(exist_ok=True)

def get_analysis_cached(log_hash: str, log_content: str):
    cache_file = cache_dir / f"{log_hash}.json"
    
    if cache_file.exists():
        return json.load(open(cache_file))
    
    # Run analysis if not cached
    agent = CIDDQAAgent()
    result = agent.analyze_and_remediate(log_content)
    
    # Store for future use
    cache_file.write_text(json.dumps(result, default=str))
    return result
```

## 📋 Project Structure

```
llm_rag_powered_qa_agent/
├── src/
│   ├── agents/               # LangChain agents
│   │   └── __init__.py      # RCAAgent, RemediationAgent, CIDDQAAgent
│   ├── rag/                 # RAG system with ChromaDB
│   │   └── __init__.py      # RAGPipeline, ChromaDBManager, DocumentProcessor
│   ├── utils/               # Utility modules
│   │   ├── parser.py        # Log parsing
│   │   ├── logger.py        # Logging setup
│   │   └── formatter.py     # Output formatting
│   ├── config.py            # Configuration management
│   └── __init__.py
├── data/
│   ├── logs/                # Sample failure logs
│   │   └── example_failure.log
│   └── documentation/       # Internal documentation
│       ├── connection_pool_guide.md
│       └── test_failure_guide.md
├── chroma_db/               # ChromaDB vector database (generated)
├── examples/
│   ├── analyze_failure.py   # Main example script
│   └── ingest_docs.py       # Documentation ingestion
├── tests/                   # Unit tests
├── requirements.txt         # Python dependencies
├── .env.example            # Environment template
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## 🔄 Workflow

### Complete Analysis Workflow

1. **Log Ingestion**: Raw CI/CD logs are parsed and normalized
2. **Error Extraction**: Key error messages and stack traces are extracted
3. **RAG Retrieval**: Relevant documentation is retrieved using semantic search
4. **RCA Analysis**: LLM analyzes logs with documentation context
5. **Root Cause Identification**: Primary and secondary causes identified
6. **Remediation Generation**: Suggested fixes generated with priority levels
7. **Result Formatting**: Results packaged as structured JSON

### Step-by-Step Process

```
Raw Log Input
    ↓
Parse & Extract Error Context
    ↓
Query RAG System (ChromaDB)
    ↓
Retrieve Relevant Documentation
    ↓
Build LLM Prompt with Context
    ↓
RCA Agent Analyzes Failure
    ↓
Identify Root Causes & Severity
    ↓
Remediation Agent Suggests Fixes
    ↓
Generate Prioritized Action Steps
    ↓
Format & Return Results
```

## 📈 Performance Metrics

### Expected Performance

- **Analysis Time**: 5-15 seconds per log (depending on log size)
- **RAG Query Time**: < 200ms
- **LLM Response Time**: 3-10 seconds
- **Memory Usage**: ~500MB baseline, scales with vector DB size

### Optimization Tips

1. **Chunk Size**: Adjust `CHUNK_SIZE` for your documentation
   - Smaller (500): Better precision, more queries
   - Larger (2000): Faster, more context per chunk

2. **Top-K Retrieval**: Set `TOP_K_RETRIEVAL` based on needs
   - Lower (1-2): Faster, risk missing context
   - Higher (5+): Slower, more comprehensive context

3. **Batch Processing**: Process multiple logs together
   - Reuse RAG initialization
   - Implement caching for similar logs

## 🔐 Security Considerations

- **API Keys**: Store securely in `.env`, never commit to version control
- **Logs**: May contain sensitive information; implement appropriate access controls
- **Documentation**: Restrict access to sensitive internal procedures
- **Vector DB**: Use appropriate file permissions on `chroma_db/` directory

## 🧪 Testing

```bash
# Run unit tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src

# Run specific test
pytest tests/test_agents.py::TestRCAAgent
```

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

## 🙋 Support & Issues

- **Bug Reports**: GitHub issues
- **Feature Requests**: GitHub discussions
- **Documentation**: See `/data/documentation/`

## 🔮 Future Roadmap

- [ ] Web UI for log analysis
- [ ] Integration with Slack/Teams
- [ ] Multi-language log support
- [ ] Historical failure pattern analysis
- [ ] Predictive failure detection
- [ ] Custom LLM model support
- [ ] Distributed processing for large logs
- [ ] Cost optimization recommendations

## 📚 Additional Resources

- [LangChain Documentation](https://docs.langchain.com/)
- [ChromaDB Guide](https://docs.trychroma.com/)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [CI/CD Best Practices](./data/documentation/)

---

**Made with ❤️ for DevOps & QA Teams**

For questions or feedback, please open an issue or reach out!
