FROM tiangolo/uwsgi-nginx-flask:python3.11

RUN pip install --upgrade pip "pipenv==2023.7.3"
COPY Pipfile Pipfile.lock ./

RUN  pipenv  install --dev --system

COPY . /app
