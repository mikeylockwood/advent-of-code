from solution import parse, solve_1, solve_2

TEST_DATA = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


def test_solve_1():
    data = parse(TEST_DATA)
    result = solve_1(data)
    assert result == 4361
    print('Test 1 passed!')


def test_solve_2():
    data = parse(TEST_DATA)
    result = solve_2(data)
    assert result == 467835
    print('Test 2 passed!')


if __name__ == '__main__':
    test_solve_1()
    test_solve_2()
