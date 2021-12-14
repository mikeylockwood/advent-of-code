from pathlib import Path


def parse(data):
    return [int(x) for x in data.strip().split(',')]


def get_data():
    data_file = Path(__file__).with_name('data.txt')

    with data_file.open('r') as f:
        data = f.read()

    return parse(data)


def solve_1(data):
    return min(sum(abs(num - x) for num in data) for x in range(max(data) + 1))


def solve_2(data):
    return min(
        sum(int((abs(num - x) * (abs(num -x) + 1)) / 2) for num in data)
        for x in range(max(data) + 1)
    )


if __name__ == '__main__':
    data = get_data()
    print('Solution 1')
    print(solve_1(data))
    print('\nSolution 2')
    print(solve_2(data))
