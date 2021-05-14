import unittest


from nest import validate_args, AlreadyPassedArgument, InvalidArgument, MissingArguments, TooManyArguments


class TestValidators(unittest.TestCase):
    body = [
        {
            "country": "US",
            "city": "Boston",
            "currency": "USD",
            "amount": 100
        }
    ]


    def test_success(self):
        arguments = ["currency", "country", "city"]
        validate_args(self.body[0].keys(), arguments)
        assert True

    def test_missing_arguments(self):
        arguments = None
        with self.assertRaises(MissingArguments):
            validate_args(self.body[0].keys(), arguments)

    def test_already_passed_argument(self):
        arguments = ["currency", "country", "country"]
        with self.assertRaises(AlreadyPassedArgument):
            validate_args(self.body[0].keys(), arguments)

    def test_invalid_argument(self):
        arguments = ["city", "country", "curr"]
        with self.assertRaises(InvalidArgument):
            validate_args(self.body[0].keys(), arguments)

    def test_too_many_arguments(self):
        arguments = ["currency", "country", "city", "amount", "somearg"]
        with self.assertRaises(TooManyArguments):
            validate_args(self.body[0].keys(), arguments)
