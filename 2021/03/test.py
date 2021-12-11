from solution_1 import solve as solve_1
from solution_2 import solve as solve_2
from utils import parse

TEST_DATA = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""


def test_solve_1():
    data = parse(TEST_DATA)
    result = solve_1(data)
    assert result == 198
    print('Test 1 passed!')


def test_solve_2():
    data = parse(TEST_DATA)
    result = solve_2(data)
    assert result == 230
    print('Test 2 passed!')


if __name__ == '__main__':
    test_solve_1()
    test_solve_2()
