import json

from gendiff.utils import is_dict


def _get_formatted_value(value):  # noqa: WPS110
    if is_dict(value):
        return '[complex value]'
    return json.dumps(value).replace('"', "'")


def _get_formatted_path(parent, key):
    return f'{parent}.{key}' if parent else key


def _get_change_diff(path, prev_value, curr_value):
    return f"Property '{path}' was updated. From {prev_value} to {curr_value}"


def _get_added_diff(path, added_value):
    return f"Property '{path}' was added with value: {added_value}"


def _get_removed_diff(path):
    return f"Property '{path}' was removed"


def _build_plain(ast, parent=''):  # noqa: WPS231
    def inner(node):
        node_type = node.get('type')
        key = node.get('key')
        full_path = _get_formatted_path(parent, key)
        previous_value = _get_formatted_value(node.get('previous_value'))
        current_value = _get_formatted_value(node.get('current_value'))

        if node_type == 'nested':
            return _build_plain(node.get('children'), full_path)
        elif node_type == 'changed':
            return _get_change_diff(full_path, previous_value, current_value)
        elif node_type == 'added':
            return _get_added_diff(full_path, current_value)
        elif node_type == 'removed':
            return _get_removed_diff(full_path)

    return '\n'.join(filter(bool, map(inner, ast)))


def format_to_plain(ast):
    return _build_plain(ast)
