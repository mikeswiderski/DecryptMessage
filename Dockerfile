FROM python:3

ENV PYTHONUNBUFFERED 1
ENV PATH="/decryptMessage:${PATH}"
RUN mkdir /decryptMessage
WORKDIR /decryptMessage
COPY . /decryptMessage/
RUN pip install -r requirements.txt

EXPOSE 80 

CMD ["gunicorn", "--bind", "80", "decryptMessage.wsgi"]
