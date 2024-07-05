# Use the official Python image as base image
FROM python:3.12-slim

WORKDIR /app

ENV POETRY_VERSION=1.8.3 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_HOME="/opt/poetry"

RUN pip install "poetry==$POETRY_VERSION" && poetry --version

COPY pyproject.toml poetry.lock /app/
RUN --mount=type=cache,target=/home/.cache/pypoetry/cache \
    --mount=type=cache,target=/home/.cache/pypoetry/artifacts \
    poetry install --no-root

# Copy the Flask application code to the container
COPY . .

# Expose the port on which your Flask app will run
EXPOSE 53336

# Command to run the Flask application
CMD ["python", "run.py"]
