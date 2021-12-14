from solution import parse, solve_1, solve_2

TEST_DATA = """
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""

result_2 = """
#####
#...#
#...#
#...#
#####
.....
.....
""".strip()



def test_solve_1():
    data = parse(TEST_DATA)
    result = solve_1(data)
    assert result == 17
    print('Test 1 passed!')


def test_solve_2():
    data = parse(TEST_DATA)
    result = solve_2(data)
    assert result == result_2
    print('Test 2 passed!')


if __name__ == '__main__':
    test_solve_1()
    test_solve_2()
