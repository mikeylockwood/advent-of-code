from solution import parse, solve_1, solve_2

TEST_DATA = "x=20..30, y=-10..-5"


def test_solve_1():
    data = parse(TEST_DATA)
    result = solve_1(data)
    assert result == 45
    print('Test 1 passed!')


def test_solve_2():
    data = parse(TEST_DATA)
    result = solve_2(data)
    assert result == 112
    print('Test 2 passed!')


if __name__ == '__main__':
    test_solve_1()
    test_solve_2()
