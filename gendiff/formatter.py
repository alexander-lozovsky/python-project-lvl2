import json
import re

from gendiff.utils import is_dict


def _get_formatted_value(value, level=0):  # noqa: WPS110
    string = re.sub('[,"]', '', json.dumps(value, indent=4))

    if not is_dict(value):
        return string

    first_line, *rest_lines = string.split('\n')
    rest_lines_with_indent = list(
        map(lambda line: (' ' * level * 4) + line, rest_lines),
    )

    return '\n'.join([first_line, *rest_lines_with_indent])


def _get_diff_line(key, value, sign=' ', indent=''):  # noqa: WPS110
    return f'{indent}  {sign} {key}: {value}'


def _build_default(ast, level=0):  # noqa: WPS212, WPS231
    def inner(node):
        indent = ' ' * level * 4
        node_type = node.get('type')
        key = node.get('key')
        previous_value = _get_formatted_value(
            node.get('previous_value'), level=level + 1,
        )
        current_value = _get_formatted_value(
            node.get('current_value'), level=level + 1,
        )

        if node_type == 'unchanged':
            return _get_diff_line(key, previous_value, indent=indent)
        elif node_type == 'changed':
            remove_line = _get_diff_line(
                key, previous_value, indent=indent, sign='-',
            )
            add_line = _get_diff_line(
                key, current_value, indent=indent, sign='+',
            )
            return f'{remove_line}\n{add_line}'
        elif node_type == 'added':
            return _get_diff_line(key, current_value, indent=indent, sign='+')
        elif node_type == 'removed':
            return _get_diff_line(key, previous_value, indent=indent, sign='-')

        children = _build_default(node.get('children'), level=level + 1)
        close_bracket_indent = indent + ' ' * 4

        return f'{indent}    {key}: {{\n{children}\n{close_bracket_indent}}}'

    return '\n'.join(map(inner, ast))


def _to_default(ast):
    formatted = _build_default(ast)
    return f'{{\n{formatted}\n}}'


formatters = {
    'default': _to_default,
}


def format_ast(ast, format_type='default'):
    formatter = formatters[format_type]
    return formatter(ast)
