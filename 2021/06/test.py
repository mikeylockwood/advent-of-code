from solution_1 import solve as solve_1
from solution_2 import solve as solve_2
from utils import parse

TEST_DATA = '3,4,3,1,2'


def test_solve_1():
    data = parse(TEST_DATA)
    result = solve_1(data)
    assert result == 5934
    print('Test 1 passed!')


def test_solve_2():
    data = parse(TEST_DATA)
    result = solve_2(data)
    assert result == 26984457539
    print('Test 2 passed!')


if __name__ == '__main__':
    test_solve_1()
    test_solve_2()
