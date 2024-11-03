install: #installs requirements
	pip install --upgrade pip && pip install -r requirements.txt
#ensures pip works?

format: #formats files
	black *.py

lint: #checks that python files are 
	#pylint --ignore-patterns=test_.*?py *.py
	ruff check *.py 

test:
	python -m pytest -cov=main test_main.py

all: install format lint test