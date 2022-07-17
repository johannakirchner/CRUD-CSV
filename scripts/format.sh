#!/bin/sh -e
set -x

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place crud-csv --exclude=__init__.py
black crud-csv
isort crud-csv
