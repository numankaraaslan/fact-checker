# tests/test_api.py
from fastapi.testclient import TestClient
from app.main import app
from app.services.tavily_client import tavily_search

client = TestClient(app)

def test_tavily_basic():
    results = tavily_search("Eiffel Tower height")
    print("\n Tavily Results:", results)
    
    # Basic sanity checks
    assert isinstance(results, list)
    assert len(results) > 0
    assert "title" in results[0]
    assert "url" in results[0]


def test_fact_check_basic():
    resp = client.post("/fact-check", json={"query": "There is nothing called chatgpt in this world"})
    print("\nOPENAPI Result:", resp.json())
    assert resp.status_code == 200
    data = resp.json()
    assert "verdict" in data
    assert "reasoning" in data
    assert "citations" in data

