from solution import parse, solve_1, solve_2

TEST_DATA = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48
0 0 50

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70
0 0 18

light-to-temperature map:
45 77 23
81 45 19
68 64 13
0 0 45

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
0 0 56
"""


def test_solve_1():
    data = parse(TEST_DATA)
    result = solve_1(data)
    print(result)
    assert result == 35
    print("Test 1 passed!")


def test_solve_2():
    data = parse(TEST_DATA)
    result = solve_2(data)
    print(result)
    assert result == 46
    print("Test 2 passed!")


if __name__ == "__main__":
    test_solve_1()
    test_solve_2()
