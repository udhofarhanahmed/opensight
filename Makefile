.PHONY: help install install-dev dev run test test-cov lint format check clean docker-build docker-run docker-compose

help:
@echo "OpenSight Pro - Development Commands"
@echo "===================================="
@echo ""
@echo "Setup:"
@echo "  make install          Install dependencies"
@echo "  make install-dev      Install dev dependencies"
@echo ""
@echo "Development:"
@echo "  make dev              Run Streamlit app"
@echo "  make run              Run Streamlit app (alias)"
@echo ""
@echo "Testing & Quality:"
@echo "  make test             Run tests"
@echo "  make test-cov         Run tests with coverage"
@echo "  make lint             Lint code"
@echo "  make format           Format code with black"
@echo "  make check            Type check with mypy"
@echo ""
@echo "Docker:"
@echo "  make docker-build     Build Docker image"
@echo "  make docker-run       Run Docker container"
@echo "  make docker-compose   Run with docker-compose"
@echo ""
@echo "Utilities:"
@echo "  make clean            Clean cache and build files"
@echo ""

install:
pip install -r requirements.txt

install-dev:
pip install -r requirements-dev.txt

dev:
streamlit run src/frontend/app.py

run:
streamlit run src/frontend/app.py

test:
pytest tests/ -v

test-cov:
pytest tests/ -v --cov=src --cov-report=html --cov-report=term

lint:
flake8 src/ --max-line-length=100
pylint src/ --disable=all --enable=E,F || true

format:
black src/ tests/ || true
isort src/ tests/ || true

check:
mypy src/ --ignore-missing-imports || true

clean:
find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
find . -type f -name "*.pyc" -delete
find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
rm -rf build/ dist/ *.egg-info/

docker-build:
docker build -f config/Dockerfile -t opensight-pro:latest .

docker-run:
docker run -p 8501:8501 opensight-pro:latest

docker-compose:
docker-compose -f config/docker-compose.yml up

docker-compose-build:
docker-compose -f config/docker-compose.yml up --build

.DEFAULT_GOAL := help
