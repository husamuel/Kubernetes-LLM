from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
import httpx

app = FastAPI()

STORAGE_SERVICE_URL = 'http://storage-service:7000/store'

llm_pipeline = None

class Prompt(BaseModel):
    prompt: str

@app.on_event("startup")
def load_llm_pipeline():
    global llm_pipeline

    MODEL_NAME = "gpt2-medium"

    llm_pipeline = pipeline("text-generation", model=MODEL_NAME)

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/generate")
async def generate(prompt: Prompt):
    global llm_pipeline

    result = llm_pipeline(
        prompt.prompt,
        max_length=20,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.8,
        repetition_penalty=1.2
    )

    try:
        async with httpx.AsyncClient() as client:
            await client.post(STORAGE_SERVICE_URL, json={
                "prompt": prompt.prompt,
                "response": result[0]["generated_text"]
            })
    except Exception as e:
        print("Error storing data:", e)

    return {"generated_text": result[0]["generated_text"]}
