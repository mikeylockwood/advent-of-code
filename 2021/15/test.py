from solution import parse, solve_1, solve_2

TEST_DATA = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""


def test_solve_1():
    data = parse(TEST_DATA)
    result = solve_1(data)
    assert result == 40
    print("Test 1 passed!")


def test_solve_2():
    data = parse(TEST_DATA)
    result = solve_2(data)
    assert result == 315
    print("Test 2 passed!")


if __name__ == '__main__':
    test_solve_1()
    test_solve_2()
