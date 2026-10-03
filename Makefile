.PHONY: setup models pilot test status env
EP ?= ep-001
setup:
	uv sync --frozen --extra dev
models:
	uv run python scripts/fetch_models.py
pilot: models
	uv run ytf all $(EP)
short:
	uv run ytf all $(EP) --format short
test:
	uv run pytest -q
status:
	uv run ytf status
env:
	bash scripts/env_check.sh
