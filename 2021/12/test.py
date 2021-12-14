from solution import parse, solve_1, solve_2

TEST_DATA_A = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

TEST_DATA_B = """
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""

TEST_DATA_C = """
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""


def test_solve_1a():
    data = parse(TEST_DATA_A)
    result = solve_1(data)
    assert result == 10
    print('Test 1a passed!')


def test_solve_1b():
    data = parse(TEST_DATA_B)
    result = solve_1(data)
    assert result == 19
    print('Test 1b passed!')


def test_solve_1c():
    data = parse(TEST_DATA_C)
    result = solve_1(data)
    assert result == 226
    print('Test 1c passed!')


def test_solve_2a():
    data = parse(TEST_DATA_A)
    result = solve_2(data)
    assert result == 36
    print('Test 2a passed!')


def test_solve_2b():
    data = parse(TEST_DATA_B)
    result = solve_2(data)
    assert result == 103
    print('Test 2b passed!')


def test_solve_2c():
    data = parse(TEST_DATA_C)
    result = solve_2(data)
    assert result == 3509
    print('Test 2c passed!')


if __name__ == '__main__':
    test_solve_1a()
    test_solve_1b()
    test_solve_1c()
    test_solve_2a()
    test_solve_2b()
    test_solve_2c()
