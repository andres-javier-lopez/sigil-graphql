#!/usr/bin/env bash

echo "Running isort"
poetry run isort --check-only .
echo "Running black"
poetry run black --check .
echo "Running pytest"
poetry run pytest
