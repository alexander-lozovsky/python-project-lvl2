from gendiff import generate_diff


class TestDefaultFormat:
    def test_json_default(self):
        res = generate_diff(
            './tests/__fixtures__/file1.json',
            './tests/__fixtures__/file2.json',
        )
        expected = open(
            './tests/__fixtures__/expected_default_format.txt', 'r',
        ).read()

        assert res == expected

    def test_yaml_default(self):
        res = generate_diff(
            './tests/__fixtures__/file1.yaml',
            './tests/__fixtures__/file2.yaml',
        )
        expected = open(
            './tests/__fixtures__/expected_default_format.txt', 'r',
        ).read()

        assert res == expected


class TestPlainFormat:
    def test_json_plain(self):
        res = generate_diff(
            './tests/__fixtures__/file1.json',
            './tests/__fixtures__/file2.json',
            format_type='plain',
        )
        expected = open(
            './tests/__fixtures__/expected_plain_format.txt', 'r',
        ).read()

        assert res == expected

    def test_yaml_default(self):
        res = generate_diff(
            './tests/__fixtures__/file1.yaml',
            './tests/__fixtures__/file2.yaml',
            format_type='plain',
        )
        expected = open(
            './tests/__fixtures__/expected_plain_format.txt', 'r',
        ).read()

        assert res == expected


class TestJsonFormat:
    def test_json_json(self):
        res = generate_diff(
            './tests/__fixtures__/file1.json',
            './tests/__fixtures__/file2.json',
            format_type='json',
        )
        expected = open(
            './tests/__fixtures__/expected_json_format.json', 'r',
        ).read()

        assert res == expected

    def test_yaml_json(self):
        res = generate_diff(
            './tests/__fixtures__/file1.yaml',
            './tests/__fixtures__/file2.yaml',
            format_type='json',
        )
        expected = open(
            './tests/__fixtures__/expected_json_format.json', 'r',
        ).read()

        assert res == expected
