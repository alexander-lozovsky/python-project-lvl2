from gendiff.utils import is_dict


def get_ast(file1, file2):
    def inner(key):
        previous_value = file1.get(key)
        current_value = file2.get(key)

        if key in file1 and key in file2:
            if previous_value == current_value:
                return {
                    'type': 'unchanged',
                    'key': key,
                    'previous_value': previous_value,
                    'current_value': current_value,
                }
            elif is_dict(previous_value) and is_dict(current_value):
                return {
                    'type': 'nested',
                    'key': key,
                    'children': get_ast(previous_value, current_value),
                }
            return {
                'type': 'changed',
                'key': key,
                'previous_value': previous_value,
                'current_value': current_value,
            }
        elif key in file2:
            return {
                'type': 'added',
                'key': key,
                'previous_value': previous_value,
                'current_value': current_value,
            }
        return {
            'type': 'removed',
            'key': key,
            'previous_value': previous_value,
            'current_value': current_value,
        }

    sorted_keys = sorted({*file1.keys(), *file2.keys()})

    return list(map(inner, sorted_keys))
