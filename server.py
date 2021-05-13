import hug

from nest import rebuild_json, validate_args, MissingArguments, InvalidArgument, TooManyArguments, AlreadyPassedArgument


@hug.post(
    requires=hug.authentication.basic(
        hug.authentication.verify("serban", "gron-drunt-crisp")
    ),
    input_format=hug.input_format.json,
    examples="keys=country,city,currency",
)
@hug.local()
def restructure(body, keys: hug.types.delimited_list(",")):
    """Restructures list of dicts to a single dict with arbitrary level of nesting"""
    try:
        validate_args(body[0].keys(), keys)
    except MissingArguments:
        return {'error': 'Please provide at least one argument (key).'}
    except InvalidArgument:
        return {'error': 'Invalid arguments. Arguments have to match JSON keys.'}
    except TooManyArguments:
        return {'error': 'More arguments than JSON keys provided.'}
    except AlreadyPassedArgument:
        return {'error': 'Duplicate arguments provided.'}
    return rebuild_json(body, keys)
