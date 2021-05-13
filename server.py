import hug

from nest import rebuild_json


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
    return rebuild_json(body, keys)
