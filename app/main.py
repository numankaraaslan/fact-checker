from fastapi import FastAPI
from .pipeline import fact_check_pipeline
from .models.schema import FactCheckRequest, FactCheckResponse

app = FastAPI(title="Fact Check Service")

@app.post("/fact-check", response_model=FactCheckResponse)
def fact_check(request: FactCheckRequest):
    verdict, reasoning, evidence = fact_check_pipeline(request.query)
    return FactCheckResponse(
        verdict=verdict,
        reasoning=reasoning,
        citations=evidence
    )
