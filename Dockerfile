FROM python:3.13.3-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE = 1 \
PYTHONUNBUFFERED = 1

WORKDIR /app

RUN apt-get update && apt-get install -y curl

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY src/requirements-docker.txt .
RUN uv pip install -r requirements-docker.txt --system

COPY src/ .

WORKDIR /app/backend

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]