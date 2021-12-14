from solution import parse, solve_1, solve_2

TEST_DATA = """
199
200
208
210
200
207
240
269
260
263
"""


def test_solve_1():
    data = parse(TEST_DATA)
    result = solve_1(data)
    assert result == 7
    print('Test 1 passed!')


def test_solve_2():
    data = parse(TEST_DATA)
    result = solve_2(data)
    assert result == 5
    print('Test 2 passed!')


if __name__ == '__main__':
    test_solve_1()
    test_solve_2()
