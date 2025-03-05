# build image
FROM mcr.microsoft.com/devcontainers/python:3.11 AS builder

WORKDIR /app_flask_archetype

ENV PIPENV_VENV_IN_PROJECT=1

ADD Pipfile.lock Pipfile /app_flask_archetype/

RUN pipenv sync

# prodcution image
FROM python:3.11-slim-bookworm AS production

RUN apt-get update && apt-get install libpq5 -y

EXPOSE 8080

WORKDIR /app_flask_archetype

ENV PYTHONUNBUFFERED=1

COPY . .

RUN mkdir .venv

COPY --from=builder  /app_flask_archetype/.venv/ .venv

RUN adduser -u 5678 --disabled-password --gecos "" app_flask_archetype && chown -R app_flask_archetype /app_flask_archetype
USER app_flask_archetype

RUN chmod +x ./entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]
