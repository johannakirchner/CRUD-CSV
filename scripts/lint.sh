#!/usr/bin/env bash

set -x

mypy crud-csv
black crud-csv --check
isort --check-only crud-csv
flake8
