import json
from pathlib import PurePosixPath
from gendiff.parser import parse

import yaml

loaders = {
    '.json': json.load,
    '.yaml': yaml.load,
    '.yml': yaml.load,
}


def generate_diff(file1_path, file2_path):
    file1 = open(file1_path)
    file2 = open(file2_path)

    file1_suffix = PurePosixPath(file1_path).suffix
    file2_suffix = PurePosixPath(file2_path).suffix

    loaded_file1 = loaders[file1_suffix](file1)
    loaded_file2 = loaders[file2_suffix](file2)

    return parse(loaded_file1, loaded_file2)
