# Minimal Django Rest
![minimal_django_rest.png](..%2F..%2FDesktop%2Fminimal_django_rest.png)

## Description
This project aims to reduce the file size and code amount in setting up a `RestFramework` in Django.

## The capabilities
The capabilities that this project is supposed to have include:
- [ ] The possibility of making tokens and managing login by knox
- [ ] A simple model
- [ ] A view to perform `CRUD` operations by the ViewSet class
- [ ] Remove useless codes

## Usage
Just run the following codes in the `terminal`:
```angular2html

python -m pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```