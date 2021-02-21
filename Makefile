install:
	poetry install

gendiff-help:
	poetry run gendiff --help

gendiff:
	poetry run gendiff ./__fixtures__/file1.json ./__fixtures__/file2.json

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

.PHONY: gendiff
