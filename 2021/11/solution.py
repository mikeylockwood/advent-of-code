from pathlib import Path


def parse(data):
    return [[int(x) for x in row] for row in data.strip().split()]


def get_data():
    data_file = Path(__file__).with_name('data.txt')

    with data_file.open('r') as f:
        data = f.read()

    return parse(data)


def add_energy(data):
    new_data = []
    flashes = []

    for y, row in enumerate(data):
        new_row = []
        for x, octopus in enumerate(row):
            new_val = octopus + 1
            if new_val == 10:
                flashes.append((x, y))
            new_row.append(new_val)
        new_data.append(new_row)

    return new_data, flashes


def apply_flash(data, adjacents, flashes):
    if len(adjacents) == 0:
        return

    x, y = adjacents.pop()
    data[y][x] += 1
    if data[y][x] == 10:
        flashes.append((x, y))

    return apply_flash(data, adjacents, flashes)


def flash(data, flashes, count=0):
    if len(flashes) == 0:
        return count

    x, y = flashes.pop()
    h = len(data)
    w = len(data[0])

    coords = [(i,j) for i in (-1,0,1) for j in (-1,0,1) if not (i == j == 0)]
    adjacents = [
        (x + i, y + j)
        for i, j in coords
        if 0 <= x + i < w
        and 0 <= y + j < h
    ]
    apply_flash(data, adjacents, flashes)
    return flash(data, flashes, count + 1)


def reset_flashes(data):
    return [[0 if x > 9 else x for x in row] for row in data]


def apply_steps(data, steps):
    count = 0
    for x in range(steps):
        data, flashes = add_energy(data)
        count += flash(data, flashes)
        data = reset_flashes(data)
    return count


def find_synced(data, step=0):
    if sum(sum(x for x in row) for row in data) == 0:
        return step

    data, flashes = add_energy(data)
    flash(data, flashes)
    data = reset_flashes(data)
    return find_synced(data, step + 1)


def solve_1(data):
    return apply_steps(data, 100)


def solve_2(data):
    return find_synced(data)


if __name__ == '__main__':
    data = get_data()
    print('Solution 1')
    print(solve_1(data))
    print('\nSolution 2')
    print(solve_2(data))
