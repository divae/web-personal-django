# Recipe App API

Source code for my Udemy course Build a [Backend REST API with Python & Django - Advanced](http://udemy.com/django-python-advanced/).

## Getting started

To start project, run:

```
docker-compose up
```

*remember create super user the first time
```
docker-compose run app sh -c "python manage.py createsuperuser"
```

The API will then be available at http://127.0.0.1:8000

## Make migrations
```
docker-compose run app sh -c "python manage.py makemigrations `modulename`"
```

## Test

To run test :
```
docker-compose run app sh -c "python manage.py test && flake8"
```