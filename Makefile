# This will output the help for each task.
# Thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.DEFAULT_GOAL := help
help: ## Show helpful information concerning the available tasks
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
.PHONY: help

install: ## Install project dependencies
	@poetry install
.PHONY: rebuild

analysis: ## Run the complete static analysis of the code
	make format
	make fimports
	make lint
.PHONY: analysis

format: ## Code formatting
	@poetry run scripts/format.sh
.PHONY: format

fimports: ## Perform import ordering and code formatting
	@poetry run scripts/format-imports.sh
.PHONY: format-imports

lint: ## Run the linting tools for the Python code base
	@poetry run scripts/lint.sh	
.PHONY: lint

start: ## Run the application
	@poetry run python crud-csv/main.py
.PHONY: teardown
