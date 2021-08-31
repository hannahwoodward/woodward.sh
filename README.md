---
title: woodward.sh
tags:
  - python
  - starlette
---

# woodward.sh

## Helpful Links

- https://www.starlette.io/
- https://railway.app/
- https://github.com/tiangolo/uvicorn-gunicorn-starlette-docker

## Setup

- Build the docker image `docker build -t starlette .`
- Start the container `docker run -d --name woodward-sh -p 80:80 starlette`
- For auto restart in development `docker run -d -p 80:80 -v $(pwd):/app starlette /start-reload.sh`
