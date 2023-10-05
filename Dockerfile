FROM node:slim as nodebuild

COPY ./app app_build

# Pre-install packages
RUN cd app_build && \
    npm i --omit=dev && \
    mkdir -p static/js && \
    rm -rf static/js/node_modules && \
    mv node_modules static/js/

FROM tiangolo/uvicorn-gunicorn:python3.11-slim as starlettebuild

RUN pip install --no-cache-dir starlette frontmatter jinja2 markdown

RUN apt-get update && apt-get install -y unzip wget

# Copy whole dir for prod
COPY --from=nodebuild app_build /app

# For live reload, copy over generated js libs to re-populate on refresh
COPY --from=nodebuild app_build/static/js /app_build/static/js
