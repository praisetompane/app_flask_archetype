#!/bin/sh

echo "Running Database Migrations"
    .venv/bin/alembic upgrade head
echo "Done Running Database Migrations\n"

echo "Starting The Application"
    .venv/bin/gunicorn --config gunicorn_config.py