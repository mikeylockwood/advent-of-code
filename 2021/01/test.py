from solution_1 import solve as solve_1
from solution_2 import solve as solve_2

TEST_DATA = """
199
200
208
210
200
207
240
269
260
263
"""


def parse_test_data():
    return [int(x) for x in TEST_DATA.strip().split()]


def test_solve_1():
    data = parse_test_data()
    result = solve_1(data)
    assert result == 7


def test_solve_2():
    data = parse_test_data()
    result = solve_2(data)
    assert result == 5


if __name__ == '__main__':
    test_solve_1()
    test_solve_2()
