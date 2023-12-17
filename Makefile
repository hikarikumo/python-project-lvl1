#install: 
#	poetry install
#
#linter:
#	poetry add --dev flake8
#
#lint:
#	poetry run flake8 brain_games
#
#selfcheck:
#	poetry check
#
#check: selfcheck lint
#
#.PHONY: install linter lint selfcheck check

install:
	poetry install

#test:
#	poetry run pytest brain_games tests

lint:
	poetry run flake8 brain_games

build: 
	poetry build

.PHONY: install test lint selfcheck check build
