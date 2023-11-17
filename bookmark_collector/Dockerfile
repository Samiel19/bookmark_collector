FROM python:3.10-slim
WORKDIR /app
RUN pip install poetry
COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "bookmark_collector.wsgi"]
