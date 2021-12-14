from pathlib import Path


def parse(data):
    lines = data.strip().split('\n')

    return [
        [
            [int(x) for x in coord.split(',')]
            for coord in line.split(' -> ')
        ]
        for line in lines
    ]


def get_data():
    data_file = Path(__file__).with_name('data.txt')

    with data_file.open('r') as f:
        data = f.read()

    return parse(data)


def solve_1(data):
    points = [[0 for x in range(1000)] for x in range(1000)]

    for a, b in data:
        ax, ay = a
        bx, by = b
        if ax == bx:
            l = abs(ay - by)
            s = ay if ay < by else by

            for num in range(0, l + 1):
                y = s + num
                points[y][ax] += 1

        elif ay == by:
            l = abs(ax - bx)
            s = ax if ax < bx else bx

            for num in range(0, l + 1):
                x =  s + num
                points[ay][x] += 1

    return sum(sum(x > 1 for x in line) for line in points)


def solve_2(data):
    points = [[0 for x in range(1000)] for x in range(1000)]

    for a, b in data:
        ax, ay = a
        bx, by = b
        if ax == bx:
            l = abs(ay - by)
            s = ay if ay < by else by

            for num in range(0, l + 1):
                y = s + num
                points[y][ax] += 1

        elif ay == by:
            l = abs(ax - bx)
            s = ax if ax < bx else bx

            for num in range(0, l + 1):
                x =  s + num
                points[ay][x] += 1

        else:
            l = abs(ax - bx)
            x_up = ax < bx
            y_up = ay < by

            for num in range(0, l + 1):
                x =  ax + num if x_up else ax - num
                y = ay + num if y_up else ay - num
                points[y][x] += 1

    return sum(sum(x > 1 for x in line) for line in points)


if __name__ == '__main__':
    data = get_data()
    print('Solution 1')
    print(solve_1(data))
    print('\nSolution 2')
    print(solve_2(data))
