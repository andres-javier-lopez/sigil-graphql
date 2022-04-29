#!/usr/bin/env bash

echo "Running isort"
poetry run isort --check-only .
echo "Running pytest"
poetry run pytest
