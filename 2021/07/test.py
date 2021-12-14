from solution import parse, solve_1, solve_2

TEST_DATA = '16,1,2,0,4,2,7,1,2,14'


def test_solve_1():
    data = parse(TEST_DATA)
    result = solve_1(data)
    assert result == 37
    print('Test 1 passed!')


def test_solve_2():
    data = parse(TEST_DATA)
    result = solve_2(data)
    assert result == 168
    print('Test 2 passed!')


if __name__ == '__main__':
    test_solve_1()
    test_solve_2()
