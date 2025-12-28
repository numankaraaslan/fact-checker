source venv/bin/activate

# Fact Check Service
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Run Tests
pytest -s

## Run Locally
python -m uvicorn app.main:app --reload

## Run in Docker
docker compose up --build

## Example Request
curl -X POST http://localhost:8000/fact-check \
     -H "Content-Type: application/json" \
     -d '{"query": "There is nothing called chatgpt in this world"}'
