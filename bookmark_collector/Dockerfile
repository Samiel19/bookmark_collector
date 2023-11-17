FROM python:3.10-slim
WORKDIR /app
RUN pip3 install poetry
COPY pyproject.toml poetry.lock /app/
RUN poetry install
RUN poetry shell
COPY . .
CMD ["poetry", "run", "gunicorn", "bookmark_collection.wsgi:application", "--bind", "0:8000"]
