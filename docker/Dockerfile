FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml README.md /app/
RUN pip install -U pip && pip install .

COPY . /app

EXPOSE 8000

CMD ["uvicorn", "src.services.api:app", "--host", "0.0.0.0", "--port", "8000"]

