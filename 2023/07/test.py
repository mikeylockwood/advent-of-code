from solution import parse, solve_1, solve_2, replace_jokers

TEST_DATA = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

TEST_JOKERS = (
    ([11, 11, 11, 11, 11], (7, [0, 0, 0, 0, 0])),
    ([11, 4, 5, 3, 3], (4, [0, 4, 5, 3, 3])),
    ([1, 2, 11, 12, 13], (2, [1, 2, 0, 12, 13])),
    ([13, 1, 11, 1, 12], (4, [13, 1, 0, 1, 12])),
)


def test_solve_1():
    data = parse(TEST_DATA)
    result = solve_1(data)
    print(result)
    assert result == 6440
    print("Test 1 passed!")


def test_solve_2():
    data = parse(TEST_DATA)
    result = solve_2(data)
    print(result)
    assert result == 5905
    print("Test 2 passed!")


def test_jokers():
    for data, expected in TEST_JOKERS:
        result = replace_jokers(data)
        print(result)
        assert result == expected


if __name__ == "__main__":
    test_solve_1()
    test_jokers()
    test_solve_2()
