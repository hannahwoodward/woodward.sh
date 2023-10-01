FROM tiangolo/uvicorn-gunicorn:python3.8-alpine3.10

RUN pip install --no-cache-dir starlette frontmatter jinja2 markdown

# Install git lfs for pulling down lfs-stored resources during deployment
RUN apk add --no-cache git-lfs

COPY ./app /app
