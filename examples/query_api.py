import requests
import sys
import os

API_URL = "http://localhost:8000/analyze"

def analyze_log_file(file_path, query=None):
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        log_content = f.read()

    payload = {
        "log_content": log_content,
        "query": query
    }

    response = requests.post(API_URL, json=payload)
    if response.status_code == 200:
        print("Analysis Result:")
        print(response.json())
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python query_api.py <log_file_path> [optional_query]")
        sys.exit(1)

    file_path = sys.argv[1]
    query = sys.argv[2] if len(sys.argv) > 2 else None
    analyze_log_file(file_path, query)