.PHONY: dev test clean build

dev:
	@echo "Starting OpenSight in development mode..."
	@docker-compose up --build

test:
	@echo "Running tests..."
	@cd backend && pytest --cov=app tests/

clean:
	@echo "Cleaning up..."
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@rm -f backend/data.db
	@rm -f opensight_report.pdf

build:
	@echo "Building Docker images..."
	@docker-compose build
