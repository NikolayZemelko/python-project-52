MANAGE := poetry run python3 manage.py
POETRY := poetry run

lint:
	@$(POETRY) flake8 ./task_manager

tests:
	@$(MANAGE) test

dev:
	@$(MANAGE) runserver --settings=task_manager.settings_dev

migrations:
	@$(MANAGE) makemigrations

migrate:
	@$(MANAGE) migrate

start:
	@$(MANAGE) runserver