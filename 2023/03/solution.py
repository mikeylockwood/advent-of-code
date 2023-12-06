from typing import Dict, List
import math
import re
from pathlib import Path


def parse(data):
    return [
        re.sub(r"(\d+|.)", r"\1,", x).rstrip(',').split(',')
        for x in data.strip().split('\n')
    ]


def get_data():
    data_file = Path(__file__).with_name('data.txt')

    with data_file.open('r') as f:
        data = f.read()

    return parse(data)


def check_adjacents(data, x, y, row_len):
    result = []
    if y > 0:
        result += check_row(data[y - 1], x, row_len)
    result += check_row(data[y], x, row_len)
    if len(data) > y + 1:
        result += check_row(data[y + 1], x, row_len)
    return result


def check_row(row, x, row_len):
    result = []
    low = max((x - 1, 0))
    high = min(x + 1, row_len - 1)
    i = -1
    for item in row:
        i += len(item)

        if i >= low and item.isdigit():
            result.append(int(item))

        if i >= high:
            break
    return result


def find_symbols(data):
    symbols = []
    for y, row in enumerate(data):
        x = 0
        for i in row:
            if i.isdigit():
                x += len(i)
                continue

            if '.' not in i:
                symbols.append((x, y))

            x += len(i)
    return symbols


def solve_1(data):
    result = 0
    symbols = find_symbols(data)
    row_len = sum(len(x) for x in data[0])
    for x, y in symbols:
        result += sum(check_adjacents(data, x, y, row_len))
    return result


def solve_2(data):
    row_len = sum(len(x) for x in data[0])
    result = 0
    for y, row in enumerate(data):
        x = 0
        for item in row:
            if item != '*':
                x += len(item)
                continue

            gear = check_adjacents(data, x, y, row_len)
            if len(gear) == 2:
                result += math.prod(gear)
            x += 1
    return result


if __name__ == '__main__':
    data = get_data()
    print('Solution 1')
    print(solve_1(data))
    print('\nSolution 2')
    print(solve_2(data))
