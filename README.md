# BookmarkCollector service


## API (server part) for bookmark storage

This service is designed for storing bookmarks and creating collections of them. Link data is taken from open graph markup or meta description.

![изображение](https://github.com/Samiel19/bookmark_collector/assets/116729352/38934722-34e8-4fc2-9dc6-8523d3b1eebf)


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

        - Install Docker

        - You need two files: "docker-compose.yml" and "bookmark_collector_start.sh"

        - Check that "docker-compose.yml" and "bookmark_collector_start.sh" are in the same
        directory

        - Go to this dir and do "chmod +x ./bookmark_collector_start.sh" in terminal

        - Run "./bookmark_collector_start.sh"

        - While first start script will collect staticfiles and makemigrations/migration.
        After this, can add superuser in terminal for using /admin endpoint

        - Use http://127.0.0.1:8000/admin/ or http://127.0.0.1:8000/swagger/ or
        http://127.0.0.1:8000/api/ or http://127.0.0.1:8000/redoc/

        - If you need to stop containers, use "cd /test_ride", "docker compose down" or
        "docker compose down --remove-orphans" to remove containers, you don`t need

        - Also, you can use this service on ip http://158.160.46.204 as http://158.160.46.204/admin/
        or http://158.160.46.204/swagger/ or http://158.160.46.204/api/ or http://158.160.46.204/redoc/

        - Test superuser on server: email: admin@admin.com, password: admin


# Code formatting

        Code corresponds PEP8.
