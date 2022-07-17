# CRUD-CSV

Python program that makes CRUD operations on a CSV file and have support for multiple instances operating in the same file. 

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [1. Getting started](#1-getting-started)
- [2. Running the project](#2-running-the-project)
- [3. Static analysis](#3-static-analysis)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## 1. Getting started

In order to run this project, you must have already properly installed and configured the following dependencies:

* [Python (v3.10.4)](https://www.python.org/downloads/)
* [Poetry (v1.1.14)](https://python-poetry.org/docs/#installation)


With both dependencies installed, you can now install the project dependencies via Poetry by running the command:
```shell
make install
```

## 2. Running the project

A Makefile was implmenented in order to automate some basic actions in the project. To find out which commands are supported, run the command:
```shell
make help
```
or simply
```shell
make
```
To run the CRUD application, run the following command
```shell
make start
```

## 3. Static analysis

To format the code base to a preset pattern, just run:
```shell
make format
```

To order the imports in each module properly and also format the code, run:
```shell
make fimports
```

To lint the Python code base, run:
```shell
make lint
```

To perform the complete static analysis in one go, just run:
```shell
make analysis
```
