install:
	poetry install

gendiff:
	poetry run gendiff --help

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

.PHONY: gendiff
