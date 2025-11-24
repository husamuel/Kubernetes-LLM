FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    TRANSFORMERS_CACHE=/app/cache

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY api_gateway.py .

RUN mkdir -p /app/cache

CMD ["uvicorn", "api_gateway:app", "--host", "0.0.0.0", "--port", "9000"]
