import json


def take_first(collection):
    return collection[0]


def get_formatted_line(pair, sign=' '):
    (key, value) = pair  # noqa: WPS110

    return f'{sign} {key}: {json.dumps(value)}'


def parse(file1, file2):  # noqa: WPS231, WPS210
    sorted_file1 = sorted(file1.items(), key=take_first)
    file2 = list(file2.items())
    diff = []

    for file1_node in sorted_file1:
        file2_node = None
        for index, (key2, value2) in enumerate(file2):
            if take_first(file1_node) == key2:
                file2_node = (key2, value2)
                file2.pop(index)
                break

        if file2_node is None:
            diff.append(get_formatted_line(file1_node, '-'))
        elif file1_node == file2_node:
            diff.append(get_formatted_line(file1_node))
        else:
            diff.append(get_formatted_line(file1_node, '-'))
            diff.append(get_formatted_line(file2_node, '+'))

    diff.extend(map(lambda node: get_formatted_line(node, '+'), file2))

    return '\n  '.join(['{', *diff]) + '\n}'
