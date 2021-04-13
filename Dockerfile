FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /decryptMessage
WORKDIR /decryptMessage
COPY . /decryptMessage/
RUN pip install -r requirements.txt

EXPOSE 80 

CMD ["gunicorn", "--bind", "80", "workers", "3", "decryptMessage.wsgi"]
