import hug

from falcon import HTTP_400, HTTPError

from nest import rebuild_json, validate_args, MissingArguments, InvalidArgument, TooManyArguments, AlreadyPassedArgument


class ClientError(HTTPError):
    def __init__(self, desc):
        super().__init__(status=HTTP_400, title='error', description=str(desc))


@hug.post(
    requires=hug.authentication.basic(
        hug.authentication.verify("serban", "gron-drunt-crisp")
    ),
    input_format=hug.input_format.json,
    examples="keys=country,city,currency",
)
@hug.local()
def restructure(body):
    """Restructures list of dicts to a single dict with arbitrary level of nesting"""
    try:
        json_from_body = body['json']
        arguments = body['arguments']
        validate_args(json_from_body[0].keys(), arguments)
        return rebuild_json(json_from_body, arguments)
    except MissingArguments:
        raise ClientError('Please provide at least one argument (key).')
    except InvalidArgument:
        raise ClientError('Invalid arguments. Arguments have to match JSON keys.')
    except TooManyArguments:
        raise ClientError('More arguments than JSON keys provided.')
    except AlreadyPassedArgument:
        raise ClientError('Duplicate arguments provided.')
    except Exception as e:
        raise ClientError(f'Internal server error. : {e}')
