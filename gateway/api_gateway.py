from fastapi import FastAPI
import httpx
from pydantic import BaseModel

app = FastAPI(title="API Gateway")

LLM_SERVICE_URL = 'http://0.0.0.0:8000/generate'

class Prompt(BaseModel):
    prompt: str

@app.get("/health")
def health():
    return {"gateway": "ok"}

@app.post("/generate")
async def generate(prompt: Prompt):
    async with httpx.AsyncClient(timeout=60.0) as client:
        resp = await client.post(LLM_SERVICE_URL, json={"prompt": prompt.prompt})
        return resp.json()

