from solution import parse, solve_1, solve_2

TEST_DATA = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""


def test_solve_1():
    data = parse(TEST_DATA)
    result = solve_1(data)
    assert result == 1656
    print('Test 1 passed!')


def test_solve_2():
    data = parse(TEST_DATA)
    result = solve_2(data)
    assert result == 195
    print('Test 2 passed!')


if __name__ == '__main__':
    test_solve_1()
    test_solve_2()
