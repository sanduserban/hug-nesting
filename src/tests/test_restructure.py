import copy
import unittest

import hug
import pytest

from nest import rebuild_json


class RestructureTest(unittest.TestCase):

    body = [
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
    ]

    success_copy = copy.deepcopy(body)
    one_level_copy = copy.deepcopy(body)

    success_body = {
        "USD": {
            "Boston": {
                "US": [
                    {
                        "amount": 100
                    }
                ]
            }
        },
        "EUR": {
            "Paris": {
                "FR": [
                    {
                        "amount": 20
                    }
                ]
            },
            "Lyon": {
                "FR": [
                    {
                        "amount": 11.4
                    }
                ]
            },
            "Madrid": {
                "ES": [
                    {
                        "amount": 8.9
                    }
                ]
            }
        },
        "GBP": {
            "London": {
                "UK": [
                    {
                        "amount": 12.2
                    }
                ]
            }
        },
        "FBP": {
            "London": {
                "UK": [
                    {
                        "amount": 10.9
                    }
                ]
            }
        }
    }

    one_level = {
        "Boston": [
            {
                "country": "US",
                "currency": "USD",
                "amount": 100
            }
        ],
        "Paris": [
            {
                "country": "FR",
                "currency": "EUR",
                "amount": 20
            }
        ],
        "Lyon": [
            {
                "country": "FR",
                "currency": "EUR",
                "amount": 11.4
            }
        ],
        "Madrid": [
            {
                "country": "ES",
                "currency": "EUR",
                "amount": 8.9
            }
        ],
        "London": [
            {
                "country": "UK",
                "currency": "GBP",
                "amount": 12.2
            },
            {
                "country": "UK",
                "currency": "FBP",
                "amount": 10.9
            }
        ]
    }


    city_country_currency = {
        "Boston": {
            "US": {
                "USD": [
                    {
                        "amount": 100
                    }
                ]
            }
        },
        "Paris": {
            "FR": {
                "EUR": [
                    {
                        "amount": 20
                    }
                ]
            }
        },
        "Lyon": {
            "FR": {
                "EUR": [
                    {
                        "amount": 11.4
                    }
                ]
            }
        },
        "Madrid": {
            "ES": {
                "EUR": [
                    {
                        "amount": 8.9
                    }
                ]
            }
        },
        "London": {
            "UK": {
                "GBP": [
                    {
                        "amount": 12.2
                    }
                ],
                "FBP": [
                    {
                        "amount": 10.9
                    }
                ]
            }
        }
    }


    def test_success(self):
        arguments = ["currency", "city", "country"]
        result = rebuild_json(self.success_copy, arguments)
        self.assertDictEqual(result, self.success_body)

    def test_no_args_recurr(self):
        arguments = []
        result = rebuild_json(self.body, arguments)
        self.assertListEqual(result, self.body)

    def test_one_level(self):
        arguments = ["city"]
        result = rebuild_json(self.one_level_copy, arguments)
        self.assertDictEqual(result, self.one_level)

    def test_multiple_levels(self):
        arguments = ["city", "country", "currency"]
        result = rebuild_json(self.body, arguments)
        self.assertDictEqual(result, self.city_country_currency)

    def test_missing_body(self):
        arguments = ["currency", "city", "country"]
        result = rebuild_json([], arguments)
        self.assertDictEqual(result, {})
