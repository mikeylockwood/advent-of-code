from solution import parse, solve_1, solve_2

TEST_DATA = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

def test_solve_1():
    data = parse(TEST_DATA)
    result = solve_1(data)
    assert result == 142
    print('Test 1 passed!')

TEST_DATA_2 = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

TEST_DATA_3 = """
6512krnnxdxzprbtlgcfoneeightwohfl
three3qs7sevenpkjone18twonek
jmone3946eightwor
5seventhreesixfivebqtjtwoneff
8lnbqbslmqmhkvzvnkmxhllpngcm9one8oneightz
"""
def test_solve_2():
    data = parse(TEST_DATA_2)
    result = solve_2(data)
    assert result == 281

    data = parse(TEST_DATA_3)
    result = solve_2(data)
    assert result == 244

    data = parse(TEST_DATA)
    result = solve_2(data)
    assert result == 142

    print('Test 2 passed!')


if __name__ == '__main__':
    test_solve_1()
    test_solve_2()
