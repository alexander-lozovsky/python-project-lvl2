from pathlib import PurePosixPath

from gendiff.ast import get_ast
from gendiff.format.formatter import format_ast
from gendiff.loader import load_file


def generate_diff(file1_path, file2_path, format_type='default'):
    with open(file1_path, 'r') as file1_object:
        with open(file2_path, 'r') as file2_object:
            file1_suffix = PurePosixPath(file1_path).suffix
            file2_suffix = PurePosixPath(file2_path).suffix

            file1 = load_file(file1_object, file1_suffix)
            file2 = load_file(file2_object, file2_suffix)
            ast = get_ast(file1, file2)

            return format_ast(ast, format_type)
