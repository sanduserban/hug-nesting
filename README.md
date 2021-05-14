# Programming:
## TASK 1

Invoke example:
`cat input.json | python nest.py currency country city`

#### Unittest
Testing commands:
`python -m unittest src.tests.test_restructure`
`python -m unittest src.tests.test_validators`


## TASK 2
1. `pip install -r requirements.txt`

2. `hug -f server.py`

3. `cat body_input.json | http --auth serban:gron-drunt-crisp POST :8000/restructure`\
  OR `cat huge.json | http --auth serban:gron-drunt-crisp POST :8000/restructure`


##### CURL TESTING:

```
curl --location --request POST 'http://127.0.0.1:8000/restructure' \
--header 'Authorization: Basic c2VyYmFuOmdyb24tZHJ1bnQtY3Jpc3A==' \
--header 'Content-Type: application/json' \
--data-raw '{
    "json": [
      {
        "country": "US",
        "city": "Boston",
        "currency": "USD",
        "amount": 100
      },
      {
        "country": "FR",
        "city": "Paris",
        "currency": "EUR",
        "amount": 20
      },
      {
        "country": "FR",
        "city": "Lyon",
        "currency": "EUR",
        "amount": 11.4
      },
      {
        "country": "ES",
        "city": "Madrid",
        "currency": "EUR",
        "amount": 8.9
      },
      {
        "country": "UK",
        "city": "London",
        "currency": "GBP",
        "amount": 12.2
      },
      {
        "country": "UK",
        "city": "London",
        "currency": "FBP",
        "amount": 10.9
      }
    ],
    "arguments": ["currency", "country", "city"]
}'
```