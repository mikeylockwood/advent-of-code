from solution_1 import solve as solve_1
from solution_2 import solve as solve_2


TEST_DATA = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


def parse_test_data():
    return [(x.split()[0], int(x.split()[1])) for x in TEST_DATA.strip().split('\n')]


def test_solve_1():
    data = parse_test_data()
    result = solve_1(data)
    assert result == 150


def test_solve_2():
    data = parse_test_data()
    result = solve_2(data)
    assert result == 900


if __name__ == '__main__':
    test_solve_1()
    test_solve_2()
