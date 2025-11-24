FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    TRANSFORMERS_CACHE=/app/cache

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY llm_service.py .

RUN mkdir -p /app/cache


CMD ["uvicorn", "llm_service:app", "--host", "0.0.0.0", "--port", "8000"]
