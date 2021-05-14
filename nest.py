import argparse
import json
import sys


class MissingArguments(Exception):
    pass


class AlreadyPassedArgument(Exception):
    pass


class InvalidArgument(Exception):
    pass


class TooManyArguments(Exception):
    pass


def validate_args(valid_keys, args):
    if not args:
        raise MissingArguments

    if len(valid_keys) < len(args):
        raise TooManyArguments

    visited_args = []
    for argument in args:
        if argument not in valid_keys:
            raise InvalidArgument
        if argument in visited_args:
            raise AlreadyPassedArgument

        visited_args.append(argument)


def rebuild_json(data, arguments):
    key_dict = {}
    if not arguments:
        return data

    for index, arg in enumerate(arguments):
        for d in data:
            if arg not in d:
                continue

            curr_value = d[arg]
            dicts_with_curr_value = [d for d in data if curr_value in d.values()]
            for visited_dict in dicts_with_curr_value:
                visited_dict.pop(arg, None)
            key_dict[curr_value] = rebuild_json(dicts_with_curr_value, arguments[index + 1:])
    return key_dict


if __name__ == '__main__':
    output = None
    parser = argparse.ArgumentParser(description='JSON Restructurer')
    parser.add_argument('arguments', nargs='*')

    args = parser.parse_args().arguments
    file_content = sys.stdin.read()
    try:
        data = json.loads(file_content)
        validate_args(data[0].keys(), args)
        output = rebuild_json(data, args)
    except MissingArguments:
        sys.stderr.write('Please provide at least one argument (key).')
    except InvalidArgument:
        sys.stderr.write('Invalid arguments. Arguments have to match JSON keys.')
    except TooManyArguments:
        sys.stderr.write('More arguments than JSON keys provided.')
    except AlreadyPassedArgument:
        sys.stderr.write('Duplicate arguments provided.')

    print(json.dumps(output), file=sys.stdout)