.PHONY: setup download ingest validate test serve demo status clean

setup:
	uv venv .venv --python 3.11
	. .venv/bin/activate && uv pip install -e ".[dev]"

download:
	. .venv/bin/activate && python scripts/download_data.py

ingest:
	. .venv/bin/activate && python scripts/ingest.py

validate:
	. .venv/bin/activate && python scripts/validate.py

test:
	. .venv/bin/activate && pytest -v tests/

serve:
	. .venv/bin/activate && budget-inspector serve

demo:
	. .venv/bin/activate && python scripts/run_demo.py

status:
	. .venv/bin/activate && budget-inspector status

clean:
	rm -rf build/ dist/ *.egg-info data/budget.duckdb data/normalized/*.parquet
