#!/bin/sh

echo "Running Database Migrations"
    alembic upgrade head
echo "Done Running Database Migrations"

echo "Starting The Application"
    flask run --debug