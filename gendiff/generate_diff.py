# flake8: noqa
import json


def take_first(x):
    return x[0]


def get_formatted_line(pair, sign=" "):
    (key, value) = pair
    return f'{sign} {key}: {json.dumps(value)}'


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))

    sorted_file1 = sorted(file1.items(), key=take_first)
    file2 = list(file2.items())
    result = []

    for file1_node in sorted_file1:
        file2_node = None
        for index, (key2, value2) in enumerate(file2):
            if take_first(file1_node) == key2:
                file2_node = (key2, value2)
                file2.pop(index)
                break

        if file2_node is None:
            result.append(get_formatted_line(file1_node, '-'))
        elif file1_node == file2_node:
            result.append(get_formatted_line(file1_node))
        else:
            result.append(get_formatted_line(file1_node, '-'))
            result.append(get_formatted_line(file2_node, '+'))

    result.extend(map(lambda item: get_formatted_line(item, '+'), file2))

    return '\n  '.join(['{', *result]) + '\n}'
