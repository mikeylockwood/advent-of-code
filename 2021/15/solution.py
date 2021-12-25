from math import inf
from collections import defaultdict
from pathlib import Path


def parse(data):
    return {
        (x, y): int(val)
        for y, row in enumerate(data.strip().split())
        for x, val in enumerate(row)
    }


def get_data():
    data_file = Path(__file__).with_name('data.txt')

    with data_file.open('r') as f:
        data = f.read()

    return parse(data)


def navigate_paths(data, stack, totals, end):
    while stack:
        x, y = min(stack)
        if (x, y) == end:
            return

        stack.remove((x, y))

        ex, ey = end
        neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for a, b in [(x + nx, y + ny) for nx, ny in neighbours]:
            if not 0 <= a <= ex or not 0 <= b <= ey:
                continue

            total = totals[(x, y)] + data[(a, b)]

            if total > totals[(a, b)]:
                continue

            totals[(a, b)] = total
            stack.add((a, b))


def find_path(data):
    totals = defaultdict(lambda: inf)
    origin = (0, 0)
    end = max(data.keys())
    totals[origin] = 0
    stack = set((origin,))
    navigate_paths(data, stack, totals, end)
    return totals[max(totals)]


def expand_data(data):
    w, h = tuple(v + 1 for v in max(data.keys()))
    xy = lambda x, y: ((data[(x % w, y % h)] + y // h + x // w) - 1) % 9 + 1

    return {
        (x, y): xy(x, y)
        for y in range(5 * w)
        for x in range(5 * h)
    }


def solve_1(data):
    return find_path(data)


def solve_2(data):
    data = expand_data(data)
    return find_path(data)


if __name__ == '__main__':
    data = get_data()
    print('Solution 1\n', solve_1(data))
    print('\nSolution 2\n', solve_2(data))
