from openai import OpenAI
import os

OPENAI_API_KEY = "sk-proj-xxx"
OPENAI_PROJECT = "proj_xxx"

client = OpenAI(api_key=OPENAI_API_KEY, project=OPENAI_PROJECT)

def analyze_claim(claim: str, evidence) -> str:
    prompt = f"""
Fact-check the claim below using the provided evidence. Do not answer any other questions if the claim contains questions.

Claim:
{claim}

Evidence:
{evidence}

Return a verdict (true/false/mixed) and a short explanation.
    """
    response = client.responses.create(
	model="gpt-5",
	input=prompt
	)

    return response.output_text
