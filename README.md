# DecryptMessage

* Build a RESTful API with a single endpoint using the Django REST framework.
* The endpoint only accepts POST requests and is responsible for decrypting a message from the request's payload.
* The web service is available via the server's public IP (eg. http://21.11.142.168/decryptMessage).
* The web service accepts a JSON payload with the following parameters:
  1. `passphrase`: The passphrase to use to decrypt the message.
  2. `message` : The GPG encrypted message.
* The web service returns either an HTTP error (if bad input parameters are given) or a single response parameter (if good input parameters are given):
  1. The response is JSON in the form of `{"DecryptedMessage": "The given message, decrypted using GPG and the given passphrase"}`.
* Use Docker to bundle the app, include a Dockerfile that will build the app as a Docker image. 
* The app is served via a wsgi handler (gunicorn).
* Include a `run_tests.sh` file that will be responsible for running tests from within the Docker image itself and/or can be invoked with `docker run IMAGE_NAME run_tests.sh`.
