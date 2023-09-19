FROM python:3.11-slim-buster

# set working directory
WORKDIR /usr/src/larry/ui/build

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update -y && apt-get upgrade -y && apt-get clean -y

# add and install requirements
COPY ui/build .

# set working directory
WORKDIR /usr/src/larry/api

COPY api .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]