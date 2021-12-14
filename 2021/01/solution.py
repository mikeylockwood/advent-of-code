from pathlib import Path


def parse(data):
    return [int(x) for x in data.strip().split('\n')]


def get_data():
    data_file = Path(__file__).with_name('data.txt')

    with data_file.open('r') as f:
        data = f.read()

    return parse(data)


def solve_1(data):
    return sum(data[x] > data[x-1] for x in range(1, len(data)))


def solve_2(data):
    return sum(
        sum(data[x-3:x]) > sum(data[x-4:x-1])
        for x in range(4, len(data) + 1)
    )


if __name__ == '__main__':
    data = get_data()
    print('Solution 1')
    print(solve_1(data))
    print('\nSolution 2')
    print(solve_2(data))
