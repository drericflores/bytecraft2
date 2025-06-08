# Makefile for ByteCraft2

PYTHON := python3
APP := main.py
SRC := core ui
TEST_DIR := tests

.PHONY: run test lint clean

## Run the main application
run:
	$(PYTHON) $(APP)

## Run all tests with pytest
test:
	pytest $(TEST_DIR)

## Lint code using flake8 (you must have it installed)
lint:
	flake8 $(SRC) $(APP)

## Remove all __pycache__ folders and *.pyc files
clean:
	find . -type d -name "__pycache__" -exec rm -r {} + ; \
	find . -type f -name "*.pyc" -delete

## Show available commands
help:
	@echo "Available targets:"
	@echo "  make run    - Run ByteCraft2 GUI"
	@echo "  make test   - Run unit tests with pytest"
	@echo "  make lint   - Lint source files with flake8"
	@echo "  make clean  - Remove __pycache__ and .pyc files"

