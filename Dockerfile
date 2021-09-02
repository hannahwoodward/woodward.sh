FROM tiangolo/uvicorn-gunicorn:python3.8-alpine3.10

RUN pip install --no-cache-dir starlette frontmatter jinja2 markdown

COPY ./app /app
