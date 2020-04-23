install: 
	poetry install
	poetry add --dev flake8

lint:
	poetry run flake8 brain_games
check:
	poetry lint
.PHONY: install lint check
