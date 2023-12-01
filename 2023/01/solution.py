from pathlib import Path
import re


def parse(data):
    return [x for x in data.strip().split('\n')]


def get_data():
    data_file = Path(__file__).with_name('data.txt')

    with data_file.open('r') as f:
        data = f.read()

    return parse(data)


def solve_1(data):
    result = 0
    match_string = "(" + "|".join(str(x) for x in range(1,10)) + ")"
    for line in data:
        matches = re.findall(match_string, line)
        x = NUMS[matches[0]]
        y = NUMS[matches[-1]]
        result += int(x + y)
    return result


NUMS = dict(zip(
    [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"
    ],
    [str(x) for x in range(1, 10)],
))

NUMS |= {str(x): str(x) for x in range(1, 10)}


def solve_2(data):
    result = 0
    match_string = "(?=(" + "|".join(NUMS.keys()) + "))"
    for line in data:
        matches = re.findall(match_string, line)
        x = NUMS[matches[0]]
        y = NUMS[matches[-1]]
        result += int(x + y)
    return result


if __name__ == '__main__':
    data = get_data()
    print('Solution 1')
    print(solve_1(data))
    print('\nSolution 2')
    print(solve_2(data))