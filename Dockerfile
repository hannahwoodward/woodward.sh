FROM tiangolo/uvicorn-gunicorn:python3.11-slim

RUN pip install --no-cache-dir starlette frontmatter jinja2 markdown

RUN apt-get update && apt-get install -y unzip wget

COPY ./app /app
