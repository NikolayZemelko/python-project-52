MANAGE := python3 manage.py
POETRY := poetry run

install:
	poetry install

lint:
	flake8 ./task_manager

shell:
	shell_plus --ipython --print-sql

test-coverage:
	coverage run manage.py test
	coverage xml --include=task_manager/* --omit=settings.py

tests:
	$(MANAGE) test

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