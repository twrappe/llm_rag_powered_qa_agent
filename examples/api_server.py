"""
FastAPI server for CI/CD QA Agent (Optional)
"""

import sys
from pathlib import Path

# Add parent directory to path so we can import src
sys.path.insert(0, str(Path(__file__).parent.parent))

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from src.agents import CIDDQAAgent
from src.rag import RAGPipeline
from src.config import settings

app = FastAPI(
    title="CI/CD Failure Analysis API",
    description="API for analyzing CI/CD failures with LLM-powered RCA",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None,
    openapi_url="/openapi.json"
)

# Initialize agent
rag_pipeline = RAGPipeline()
agent = CIDDQAAgent(rag_pipeline)


class AnalysisRequest(BaseModel):
    """Request model for failure analysis"""
    log_content: str
    query: Optional[str] = None


class AnalysisResponse(BaseModel):
    """Response model for analysis results"""
    status: str
    rca: dict
    remediation_suggestions: list
    rag_stats: dict


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "CI/CD Failure Analysis API"
    }


@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_failure(request: AnalysisRequest):
    """
    Analyze CI/CD failure logs.
    
    Args:
        request: AnalysisRequest with log_content and optional query
        
    Returns:
        AnalysisResponse with RCA and remediation suggestions
    """
    try:
        result = agent.analyze_and_remediate(
            request.log_content,
            request.query
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/stats")
async def get_stats():
    """Get RAG system statistics"""
    return rag_pipeline.get_stats()


if __name__ == "__main__":
    import uvicorn
    print(f"🚀 Starting CI/CD Failure Analysis API...")
    print(f"📍 Server: http://{settings.api_host}:{settings.api_port}")
    print(f"📚 Interactive Docs: http://{settings.api_host}:{settings.api_port}/docs")
    
    uvicorn.run(
        app,
        host=settings.api_host,
        port=settings.api_port,
        log_level="info"
    )
