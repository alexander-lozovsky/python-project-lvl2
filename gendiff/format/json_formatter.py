import json


def _build_json(ast):
    return json.dumps(ast, indent=4)


def format_to_json(ast):
    return _build_json(ast)
