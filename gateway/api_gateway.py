from fastapi import FastAPI
import httpx
from pydantic import BaseModel

app = FastAPI(title="API Gateway")

LLM_SERVICE_URL = 'http://llm-service:8000/generate'
STORAGE_SERVICE_URL = 'http://storage-service:7000/store'

class Prompt(BaseModel):
    prompt: str

@app.get("/health")
def health():
    return {"gateway": "ok"}

@app.post("/generate")
async def generate(prompt: Prompt):
    async with httpx.AsyncClient(timeout=60.0) as client:
        resp = await client.post(LLM_SERVICE_URL, json={"prompt": prompt.prompt})
        data = resp.json()

        return data
