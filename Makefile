#PROJECT_NAME := $(shell python setup.py --name)
#PROJECT_VERSION := $(shell python setup.py --version)
#TEST_PATH=./tinder_api/tests

.PHONY: requirements env build install tests examples clean-pyc clean-build

requirements:
	@echo 'Install python3 requirements into a linux machine'
	sudo apt-get -y install python3-pip python3-venv
	pip3 install --user --upgrade pip
	pip3 install virtualenv --user

env:
	@echo 'Install requirements into virtualenv'
	python3 -m venv .venv
	.venv/bin/pip3 install -r requirements.txt
	#source .venv/bin/activate

build:
	@echo 'Build library'
	python3 setup.py build

install: build
	@echo 'Install libary'
	python3 setup.py install

tests:
	@echo 'Run tests'
	python3 -m pytest
	# --doctest-modules

examples:
	@echo 'Run example notebooks'
	jupyter notebook --notebook-dir=./examples/

clean-pyc:
	find . -type d -name '__pycache__' -exec rm --force --recursive {} +
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	name '*~' -exec rm --force  {} 

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info
