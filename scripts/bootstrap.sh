#!/bin/bash
set -e

echo "=== BOOTSTRAP ENVIRONMENT FOR BUDGET INSPECTOR ==="

uv venv .venv --python 3.11
source .venv/bin/activate
uv pip install -e ".[dev]"

echo "✓ Virtual environment set up and package installed."
echo "Running data pipeline ingestion..."
python scripts/ingest.py
python scripts/validate.py

echo "=== ENVIRONMENT READY ==="
