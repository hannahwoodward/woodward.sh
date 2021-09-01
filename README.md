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
- https://docs.railway.app
- https://github.com/tiangolo/uvicorn-gunicorn-starlette-docker

## Setup

- Build the docker image `docker build -t starlette .`
- Start the container `docker run -d --name woodward-sh -p 80:80 starlette`
- For auto restart in development `docker run -d -p 80:80 -v $(pwd)/app:/app starlette /start-reload.sh`

## Deployment

This app is deployed to Railway - [read the docs](https://docs.railway.app/getting-started) to get started.

Dev - `railway run`
Deploy - `railway up`

Note: Front-end IP checking has been disabled via Railway env, as Railway IPs change - see https://docs.gunicorn.org/en/stable/settings.html?highlight=proxy#proxy-allow-ips
