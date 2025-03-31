FROM python:3.12.8-bookworm
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


ADD requirements.txt /tmp
RUN pip install --upgrade pip
RUN python3 -m pip install gunicorn
RUN python3 -m pip install -r /tmp/requirements.txt

RUN mkdir /app
WORKDIR /app


CMD python3 manage.py makemigrations --noinput && \
    while !(python3 manage.py migrate --noinput) do sleep 1; done && \
    python3 manage.py collectstatic --noinput && \
    gunicorn -b 0.0.0.0:8000 cinema_ticket.wsgi --reload