# Install python
FROM python:3.10.6
# Setup env
ENV PYTHONUNBUFFERED=1
ENV PIPENV_VENV_IN_PROJECT=1
# Set workdir
WORKDIR /app

#Install & use pipenv
COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --dev --system --deploy

# Copy files from apps
COPY files .

CMD ["uvicorn", "main:app",  "--host",  "0.0.0.0", "--port", "8000"]
EXPOSE 8000
