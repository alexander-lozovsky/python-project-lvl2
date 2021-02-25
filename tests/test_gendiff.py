from gendiff.generate_diff import generate_diff


def test_gendiff():
    res = generate_diff(
        './tests/__fixtures__/file1.json',
        './tests/__fixtures__/file2.json',
    )
    expected = open('./tests/__fixtures__/expected.txt', 'r').read()
    print(expected)
    print(res)
    assert res == expected
