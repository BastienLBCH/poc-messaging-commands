FROM python:3.10-buster

ADD . /app/
WORKDIR /app

ENV KEYCLOAK_PUBLIC_KEY=""
ENV KEYCLOAK_ALG=""
ENV BOOTSTRAP_SERVER=""
ENV TOPIC=""
ENV ENV=""

RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && python manage.py migrate

EXPOSE 80

CMD python -m uvicorn pocMessagingServiceCommands.asgi:application --host 0.0.0.0 --port 80