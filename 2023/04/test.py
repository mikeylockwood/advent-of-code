from solution import parse_1, parse_2, solve_1, solve_2

TEST_DATA = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

TEST_DATA_2 = """
"""


def test_solve_1():
    data = parse_1(TEST_DATA)
    result = solve_1(data)
    print(result)
    assert result == 13
    print('Test 1 passed!')


def test_solve_2():
    data = parse_2(TEST_DATA)
    result = solve_2(data)
    print(result)
    assert result == 30
    print('Test 2 passed!')


if __name__ == '__main__':
    test_solve_1()
    test_solve_2()
