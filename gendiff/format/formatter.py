from gendiff.format.default_formatter import format_to_default
from gendiff.format.json_formatter import format_to_json
from gendiff.format.plain_formatter import format_to_plain

formatters = {
    'default': format_to_default,
    'stylish': format_to_default,
    'plain': format_to_plain,
    'json': format_to_json,
}


def format_ast(ast, format_type='default'):
    formatter = formatters[format_type]
    return formatter(ast)
