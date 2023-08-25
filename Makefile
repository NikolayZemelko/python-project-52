MANAGE := poetry run python3 manage.py
POETRY := poetry run

install:
	poetry install

lint:
	$(POETRY) flake8 ./task_manager

shell:
	$(MANAGE) shell_plus --ipython --print-sql

test-coverage:
	$(POETRY) coverage run manage.py test
	$(POETRY) coverage xml --include=task_manager/* --omit=settings.py

tests:
	$(MANAGE) test

dev:
	$(MANAGE) runserver --settings=task_manager.settings_dev

migrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

PORT ?= 8000
start:
	$(POETRY) gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi