FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY Pipfile /code/
RUN pip install pipenv
RUN pipenv install --dev
COPY . /code/