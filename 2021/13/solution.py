from pathlib import Path


def parse(data):
    return data.strip().split('\n\n')


def get_data():
    data_file = Path(__file__).with_name('data.txt')

    with data_file.open('r') as f:
        data = f.read()

    return parse(data)


def get_grid(data):
    coords = [(int(row.split(',')[0]), int(row.split(',')[1])) for row in data[0].split('\n')]
    w, h = max(x for x, _ in coords) + 1, max(y for _, y in coords) + 1
    grid = [[0 for _ in range(w)] for _ in range(h)]

    for x, y in coords:
        grid[y][x] = 1

    return grid


def get_folds(data):
    return [(row.split('=')[0][-1], int(row.split('=')[1])) for row in data[1].split('\n')]


def fold_x(grid, idx):
    return [
        [x or grid[i][-j-1] for j, x in enumerate(row[:idx])]
        for i, row in enumerate(grid)
    ]


def fold_y(grid, idx):
    return [
        [x or grid[-i-1][j] for j, x in enumerate(row)]
        for i, row in enumerate(grid[:idx])
    ]


def fold_grid(grid, folds):
    if len(folds) == 0:
        return grid

    axis, idx = folds.pop(0)
    if axis == 'x':
        grid = fold_x(grid, idx)
    else:
        grid = fold_y(grid, idx)

    return fold_grid(grid, folds)


def make_code(grid):
    return '\n'.join([
        ''.join([(x and '#') or '.' for x in row]) for row in grid
    ])


def sum_grid(grid):
    return sum(sum(row) for row in grid)


def solve_1(data):
    grid = get_grid(data)
    folds = [get_folds(data)[0]]
    after = fold_grid(grid, folds)
    return sum_grid(after)


def solve_2(data):
    grid = get_grid(data)
    folds = get_folds(data)
    after = fold_grid(grid, folds)
    return make_code(after)


if __name__ == '__main__':
    data = get_data()
    print('Solution 1')
    print(solve_1(data))
    print('\nSolution 2')
    print(solve_2(data))
