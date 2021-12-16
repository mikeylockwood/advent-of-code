from itertools import pairwise
from pathlib import Path


def parse(data):
    return data.strip().split('\n\n')


def get_data():
    data_file = Path(__file__).with_name('data.txt')

    with data_file.open('r') as f:
        data = f.read()

    return parse(data)


def get_polymer(data):
    return list(data[0])


def get_codes(data):
    return {
        row.split(' -> ')[0]: row.split(' -> ')[1]
        for row in data[1].split('\n')
    }


def get_counts(polymer, codes):
    m = len(polymer)
    singles = {c: 0 for c in set(codes.values())}
    pairs = {c: 0 for c in codes}

    for a, b in pairwise(polymer):
        singles[a] += 1
        pairs[a+b] += 1

    singles[polymer[-1]] += 1

    return singles, pairs


def form_polymer(codes, singles, pairs, steps):
    if steps == 0:
        return singles

    steps -= 1

    new_pairs = {c: 0 for c in pairs}

    for k, count in pairs.items():
        if not count:
            continue

        x = codes[k]
        a, b = k[0] + x, x + k[1]
        new_pairs[a] += count
        new_pairs[b] += count
        singles[x] += count

    return form_polymer(codes, singles, new_pairs, steps)


def solve(data, steps=10):
    polymer = get_polymer(data)
    codes = get_codes(data)
    singles, pairs = get_counts(polymer, codes)
    counts = form_polymer(codes, singles, pairs, steps)
    return max(counts.values()) - min(counts.values())


if __name__ == '__main__':
    data = get_data()
    print('Solution 1')
    print(solve(data))
    print('\nSolution 2')
    print(solve(data, 40))
