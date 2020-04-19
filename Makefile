install: lint
	poetry install
lint:
	poetry run flake8 brain_gamesw