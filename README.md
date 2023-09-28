# Django-postgress-app

## Docker commands
docker-compose build
docker-compose up

## Create app
docker-compose run --rm app sh -c "django-admin startproject app ."
## Linter
docker-compose run --rm app sh -c "flake8"
