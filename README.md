# Django-postgress-app

### Docker commands
docker-compose build
docker-compose up

### Create django admin user
docker-compose run --rm app sh -c "python manage.py createsuperuser"

### Create app
docker-compose run --rm app sh -c "django-admin startproject app ."
### Linter
docker-compose run --rm app sh -c "flake8"
