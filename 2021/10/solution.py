from pathlib import Path


def parse(data):
    return data.strip().split()


def get_data():
    data_file = Path(__file__).with_name('data.txt')

    with data_file.open('r') as f:
        data = f.read()

    return parse(data)


opener = '[({<'
matches = {
    '}': '{',
    ']': '[',
    ')': '(',
    '>': '<',
    '[': ']',
    '{': '}',
    '(': ')',
    '<': '>',
}


def solve_1(data):
    scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    total = 0

    for row in data:

        opens = []
        for x in row:
            if x in opener:
                opens.append(x)
                continue

            opened = opens.pop(-1)
            if opened == matches[x]:
                continue

            else:
                total += scores[x]
                break

    return total


def solve_2(data):
    scores = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    s = []


    for row in data:
        valid = True

        total = 0
        line = []
        opens = []
        for x in row:
            if x in opener:
                opens.append(x)
                continue

            opened = opens.pop(-1)
            if opened == matches[x]:
                continue

            else:
                valid = False
                break

        if not valid:
            continue

        for x in opens[::-1]:
            close = matches[x]
            total = (total * 5) + scores[close]

        s.append(total)
        s.sort()

    return s[len(s) // 2]


if __name__ == '__main__':
    data = get_data()
    print('Solution 1')
    print(solve_1(data))
    print('\nSolution 2')
    print(solve_2(data))
