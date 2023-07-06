MANAGE := poetry run python3 manage.py

dev:
	@$(MANAGE) runserver

migrations:
	@$(MANAGE) makemigrations

migrate:
	@$(MANAGE) migrate

start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer.app:app