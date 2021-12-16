from solution import parse, solve

TEST_DATA = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""


def test_solve_1():
    data = parse(TEST_DATA)
    result = solve(data)
    assert result == 1588
    print('Test 1 passed!')


def test_solve_2():
    data = parse(TEST_DATA)
    result = solve(data, 40)
    assert result == 2188189693529
    print('Test 2 passed!')


if __name__ == '__main__':
    test_solve_1()
    test_solve_2()
