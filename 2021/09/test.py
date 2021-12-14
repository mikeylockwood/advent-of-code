from solution import parse, solve_1, solve_2

TEST_DATA = """
2199943210
3987894921
9856789892
8767896789
9899965678
"""


def test_solve_1():
    data = parse(TEST_DATA)
    result = solve_1(data)
    assert result == 15
    print('Test 1 passed!')


def test_solve_2():
    data = parse(TEST_DATA)
    result = solve_2(data)
    assert result == 1134
    print('Test 2 passed!')


if __name__ == '__main__':
    test_solve_1()
    test_solve_2()
