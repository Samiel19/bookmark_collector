#!/bin/sh


FILE=./test_ride
if [ -d "$FILE" ]
then
cd ./test_ride
docker compose down
docker pull samiel19/bookmark_collector
docker pull samiel19/bookmark_collector_gateway
docker compose -f docker-compose.yml up -d
else
mkdir test_ride test_ride/bookmark_collector
cp ./docker-compose.yml ./test_ride/
touch ./test_ride/bookmark_collector/.env
printf "ALLOWED_HOSTS=127.0.0.1, 0.0.0.0, localhost\n
POSTGRES_USER=django_user
POSTGRES_PASSWORD=mysecretpassword
POSTGRES_DB=django
DB_HOST=db
DB_PORT=5432" >> ./test_ride/bookmark_collector/.env
cd ./test_ride
docker compose -f docker-compose.yml up -d
docker compose -f docker-compose.yml exec bookmark_collector python manage.py collectstatic
docker compose -f docker-compose.yml exec bookmark_collector cp -r collected_static/ ../bookmark_collector_static/static
docker compose -f docker-compose.yml exec bookmark_collector python manage.py makemigrations user
docker compose -f docker-compose.yml exec bookmark_collector python manage.py makemigrations bookmark
docker compose -f docker-compose.yml exec bookmark_collector python manage.py migrate
echo "Create superuser account now:"
docker compose -f docker-compose.yml exec bookmark_collector python manage.py createsuperuser
fi
