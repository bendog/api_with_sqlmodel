FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Install pipenv
RUN pip3 install -U pipenv
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pipenv install --system --deploy

COPY . /app
# COPY alembic.ini alembic.ini
COPY prestart.sh prestart.sh
COPY README.md README.md
# ENV TIMEOUT=180
# ENV APP_MODULE=app.main:app 