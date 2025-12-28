from .services.tavily_client import tavily_search
from .services.llm_client import analyze_claim

def fact_check_pipeline(query: str):
    evidence = tavily_search(query)
    reasoning = analyze_claim(query, evidence)

    first_line = reasoning.splitlines()[0].lower()
    verdict = next((v for v in ["true","false","mixed"] if v in first_line), "unknown")

    return verdict, reasoning, evidence

