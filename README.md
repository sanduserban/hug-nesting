Programming:


# TASK 1

Invoke example:
cat input.json | python nest.py currency country city

# TASK 2
pip install -r requirements.txt

hug -f server.py

cat input.json | http --auth serban:gron-drunt-crisp POST :8000/restructure keys=='currency,country,city'

OR 

cat huge.json | http --auth serban:gron-drunt-crisp POST :8000/restructure keys=='currency,country,city'


POSTMAN TESTING:

POST http://127.0.0.1:8000/restructure?keys=currency,country

For the given hardcoded credentials (serban:gron-drunt-crisp) use base64 encoding of the credentials:
Headers:
Authorization: Basic c2VyYmFuOmdyb24tZHJ1bnQtY3Jpc3A==

Params:
keys=currency,country,city

Body:

JSON input