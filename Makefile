PY := $(shell if [ -x .venv/bin/python ]; then echo .venv/bin/python; else which python3; fi)
PIP := $(shell if [ -x .venv/bin/pip ]; then echo .venv/bin/pip; else which pip3 || which pip; fi)

.PHONY: venv install dev test lint format run api clean

venv:
	@test -d .venv || (python3 -m venv .venv && . .venv/bin/activate && pip install -U pip)

install: venv
	$(PIP) install -e .

dev: venv
	$(PIP) install -e ".[dev]"

test:
	pytest -q

lint:
	ruff check .
	mypy src
	bandit -q -r src || true

format:
	black .
	ruff check --fix .

run:
	APP_ENV?=dev
	APP_ENV=$(APP_ENV) $(PY) -m src.app "کاربردهای محاسبات کوانتومی در پزشکی"

api:
	APP_ENV?=dev
	$(PY) -m uvicorn src.services.api:app --host 0.0.0.0 --port 8000 --reload

clean:
	rm -rf .venv .pytest_cache .mypy_cache .ruff_cache dist build *.egg-info
