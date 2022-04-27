#!/usr/bin/env bash

poetry run python --version
poetry run python -m uvicorn sigil.app:app --host 0.0.0.0 --port $PORT --log-level warning
