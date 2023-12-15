MANAGE := python3 manage.py
POETRY := poetry run

install:
	poetry install

lint:
	$(POETRY) flake8 .

shell:
	shell_plus --ipython --print-sql

test-coverage:
	$(POETRY) coverage run manage.py test
	$(POETRY) coverage xml --include=task_manager/* --omit=settings.py

tests:
	$(POETRY) $(MANAGE) test

dev:
	$(MANAGE) runserver

migrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

PORT ?= 8000
start:
	gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi

docker-start:
	$(POETRY) pip freeze > requirements.txt
	docker-compose build --no-cache
	docker-compose up