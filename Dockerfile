FROM python:3.8-alpine

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt 

# runtime Configuration 
EXPOSE 3000
CMD ["gunicorn", "-b", "0.0.0.0:3000", "analitica:app"]

