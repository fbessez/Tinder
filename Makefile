requirements:
	sudo apt-get install python3-pip python3-venv
	sudo pip3 install virtualenv

env:
	@echo 'Install requirements into virtualenv'
	python3 -m venv .venv
	.venv/bin/pip3 install -r requirements.txt
	#source .venv/bin/activate

build:
	@echo 'Build library'
	python setup.py build

install: build
	@echo 'Install libary'
	python setup.py install

tests: build install
	@echo 'Run tests'
	python -m pytest --doctest-modules