MANAGE := poetry run python3 manage.py
POETRY := poetry run

install:
	poetry install

lint:
	@$(POETRY) flake8 ./task_manager

shell:
	@$(MANAGE) shell_plus --ipython --print-sql

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