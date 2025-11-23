from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

app = FastAPI()

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

    return {"generated_text": result[0]["generated_text"]}
