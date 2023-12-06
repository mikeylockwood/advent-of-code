from pathlib import Path
import re


def parse_1(data):
    data = re.sub(r'(\n)?Card \d+:', '\n', data)
    return [x.split("|") for x in data.strip().split('\n')]


def get_data_1():
    data_file = Path(__file__).with_name('data.txt')

    with data_file.open('r') as f:
        data = f.read()

    return parse_1(data)


def parse_2(data):
    data = re.sub(r'(\n)?Card ', '\n', data)
    parsed = {}
    for x in data.strip().split('\n'):
        num, card = x.split(':')
        wins, line = card.split("|")
        parsed[int(num)] = {
            "wins": wins,
            "line": line,
            "count": 1,
        }

    return parsed


def get_data_2():
    data_file = Path(__file__).with_name('data.txt')

    with data_file.open('r') as f:
        data = f.read()

    return parse_2(data)


def solve_1(data):
    result = 0
    for line in data:
        hits = 0
        wins, nums = line
        for x in nums.split():
            if x and f" {x} " in wins:
                hits += 1

        if hits:
            result += 2 ** (hits - 1)

    return result


def solve_2(data):
    for card in sorted(data.keys()):

        hits = 0
        wins = data[card]["wins"]
        nums = data[card]["line"]
        count = data[card]["count"]

        for x in nums.split():
            if x and f" {x} " in wins:
                hits += 1

        for x in range(hits):
            win = data.get(card + x + 1)
            if win:
                win["count"] += count

    return sum(data[x]["count"] for x in data)


if __name__ == '__main__':
    data = get_data_1()
    print('Solution 1')
    print(solve_1(data))
    data = get_data_2()
    print('\nSolution 2')
    print(solve_2(data))
