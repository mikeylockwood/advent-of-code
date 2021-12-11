from solution_1 import solve as solve_1
from solution_2 import solve as solve_2
from utils import parse


TEST_DATA = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


def test_solve_1():
    data = parse(TEST_DATA)
    result = solve_1(data)
    assert result == 150


def test_solve_2():
    data = parse(TEST_DATA)
    result = solve_2(data)
    assert result == 900


if __name__ == '__main__':
    test_solve_1()
    test_solve_2()
