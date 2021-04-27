FROM python:3

ENV PATH="/decryptMessage/:${PATH}"
RUN mkdir /decryptMessage
WORKDIR /decryptMessage
COPY . /decryptMessage/
RUN pip install -r requirements.txt

RUN chmod 755 /decryptMessage/run_tests.sh

EXPOSE 80 

CMD ["gunicorn", "--bind", ":80", "DecryptMessage.wsgi"]
