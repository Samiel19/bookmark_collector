# BookmarkMaker service


## API (server part) for bookmark storage

This service is designed for storing bookmarks and creating collections of them. Link data is taken from open graph markup or meta description.

[github](https://github.com/Samiel19)

## Technology stack
The following technologies were used in the development of this application:

- Python 3.11

- Django REST Framework

- PostgreSQL

- Docker

- Beautiful soup

- Poetry

- Djoser

## Project functionality

The user can register in the service by specifying a username, email and password. Access in the future occurs by email and password. After registration, the user can add bookmarks and create collections of them. When adding a bookmark, the user indicates only the link itself, the remaining data is taken from the markup. If there is no data, an appropriate note is placed.

The following fields are marked:
title, description, type, image.

The user can add one link once. The user sees only his own links.

Links can be added to collections, the names of the collections are unique.
You can only add your own links. When you delete a collection, the links are not deleted.



# Infrastructure

        1. The project works with the PostgreSQL DBMS.

        2. The project is hosted in three Docker containers:
            nginx, PostgreSQL and backend.

        3. The project container is updated on Docker Hub.

# Testing and deploy

        For deploy:

        - Use docker-compose.yml

        - docker compose -f docker-compose.yml up

        - docker compose -f docker-compose.yml exec bookmark_collector python manage.py collectstatic

        - docker compose -f docker-compose.yml exec bookmark_collector cp -r collected_static/ ../bookmark_collector_static/static

        - docker compose -f docker-compose.yml exec bookmark_collector python manage.py migrate

        - use http://127.0.0.1:8000/admin/ or http://127.0.0.1:8000/swagger/ or http://127.0.0.1:8000/api/ or
        http://127.0.0.1:8000/redoc/

        Test DB data:

        POSTGRES_USER=django_user
        POSTGRES_PASSWORD=mysecretpassword
        POSTGRES_DB=django
        DB_HOST=db
        DB_PORT=5432

        Test superuser: email admin@admin.com, password admin


# Code formatting

        Code corresponds PEP8.
