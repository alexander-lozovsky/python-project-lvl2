# flake8: noqa
import json


def take_first(x):
    return x[0]


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
            result.append(f'  - {file1_node[0]}: {file1_node[1]}')
        elif file1_node == file2_node:
            result.append(f'    {file1_node[0]}: {file1_node[1]}')
        else:
            result.append(f'  - {file1_node[0]}: {file1_node[1]}')
            result.append(f'  + {file2_node[0]}: {file2_node[1]}')
    result.extend(map(lambda item: f'  + {item[0]}: {item[1]}', file2))

    return '\n '.join(['{', *result, '}'])
