import hug
import pytest

from nest import validate_args, AlreadyPassedArgument, InvalidArgument, MissingArguments, TooManyArguments

body = [
        {
            "country": "US",
            "city": "Boston",
            "currency": "USD",
            "amount": 100
        }
    ]


def test_success():
    arguments = ["currency", "country", "city"]
    validate_args(body[0].keys(), arguments)
    assert True


def test_missing_arguments():
    arguments = None
    with pytest.raises(MissingArguments):
        validate_args(body[0].keys(), arguments)


def test_already_passed_argument():
    arguments = ["currency", "country", "country"]
    with pytest.raises(AlreadyPassedArgument):
        validate_args(body[0].keys(), arguments)


def test_invalid_argument():
    arguments = ["city", "country", "curr"]
    with pytest.raises(InvalidArgument):
        validate_args(body[0].keys(), arguments)


def test_too_many_arguments():
    arguments = ["currency", "country", "city", "amount", "somearg"]
    with pytest.raises(TooManyArguments):
        validate_args(body[0].keys(), arguments)
