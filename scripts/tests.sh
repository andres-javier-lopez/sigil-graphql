#!/usr/bin/env bash

echo "Running isort"
poetry run isort --check-only .
echo "Running black"
poetry run black --check .
echo "Running flake8"
poetry run flake8 sigil
echo "Running pytest"
poetry run pytest --use-database
