FROM python:3.8-alpine

ADD . /app
WORKDIR /app

RUN apk add gcc py3-pip libffi-dev autoconf automake g++ make --no-cache

RUN pip install -r requirements.txt 

# runtime Configuration 
EXPOSE 3000
CMD ["gunicorn", "-b", "0.0.0.0:3000", "analitica:app"]

