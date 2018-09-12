.PHONY: test
.PHONY: upload
.PHONY: deps
.PHONY: clean

test:
	python -m unittest discover -s tests -v

build:
	python setup.py sdist bdist_wheel

upload:
	twine upload dist/*

deps:
	pip install -r requirements.txt

clean:
	rm -rf build dist *.egg-info