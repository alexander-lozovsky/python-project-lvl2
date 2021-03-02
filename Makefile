install:
	poetry install

gendiff-help:
	poetry run gendiff --help

gendiff:
	poetry run gendiff ./tests/__fixtures__/file1.json ./tests/__fixtures__/file2.json --format=$(F)

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

test:
	poetry run pytest --cov=gendiff tests/

test-watch:
	poetry run ptw

lint:
	poetry run flake8 gendiff

.PHONY: gendiff test
