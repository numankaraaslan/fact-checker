# Mapping Note

Azure ML Prompt Flow → FastAPI

Inputs:
- promptflow: query (string)
- fastapi: request.query

Outputs:
- promptflow: verdict, reasoning, citations
- fastapi: FactCheckResponse (verdict, reasoning, citations)

Flow:
PromptFlow nodes:
Tavily search → LLM reasoning → structured output

Replaced by:
tavily_client.py → llm_client.py → fact_check_pipeline
