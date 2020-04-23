install: 
	poetry install
lint:
	poetry run flake8 brain_games
check:
	poetry lint
.PHONY: install lint check
