start:
	cd backend && python manage.py runserver
prod:
	gunicorn --pythonpath backend app.wsgi