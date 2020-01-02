FROM python:3-alpine

ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache gcc postgresql-dev postgresql-client python-dev musl-dev linux-headers

ENV DJANGO_ROOT /usr/src/app
RUN mkdir -p $DJANGO_ROOT

WORKDIR $DJANGO_ROOT

COPY ./cornershop-test-api .
COPY ./docker/django/gunicorn.py /etc/.

RUN pip install -r requirements.txt

EXPOSE 4545
CMD ["gunicorn", "cornershop-test-api.wsgi", "-c", "/etc/gunicorn.py"]
