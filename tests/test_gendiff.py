from gendiff.generate_diff import generate_diff


def test_json():
    res = generate_diff(
        './tests/__fixtures__/file1.json',
        './tests/__fixtures__/file2.json',
    )
    expected = open('./tests/__fixtures__/expected.txt', 'r').read()

    assert res == expected


def test_yaml():
    res = generate_diff(
        './tests/__fixtures__/file1.yaml',
        './tests/__fixtures__/file2.yaml',
    )
    expected = open('./tests/__fixtures__/expected.txt', 'r').read()

    assert res == expected
