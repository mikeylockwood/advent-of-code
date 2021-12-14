from pathlib import Path


def parse(data):
    return [[int(x) for x in row] for row in data.strip().split()]


def get_data():
    data_file = Path(__file__).with_name('data.txt')

    with data_file.open('r') as f:
        data = f.read()

    return parse(data)


def find_low_points(data):
    low_points = []
    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            adjacents = []
            if y > 0:
                adjacents.append(data[y-1][x])
            if y < len(data) - 1:
                adjacents.append(data[y+1][x])
            if x > 0:
                adjacents.append(row[x-1])
            if x < len(row) - 1:
                adjacents.append(row[x+1])
            if cell < min(adjacents):
                low_points.append((x,y))

    return low_points


def find_neighbours(data, stack, visited):
    if not stack:
        return

    x, y = stack.pop()

    if data[y][x] == 9 or (x, y) in visited:
        return find_neighbours(data, stack, visited)

    visited.append((x, y))

    if y > 0:
        stack.append((x, y - 1))
    if y < len(data) - 1:
        stack.append((x, y + 1))
    if x > 0:
        stack.append((x - 1, y))
    if x < len(data[0]) - 1:
        stack.append((x + 1, y))

    return find_neighbours(data, stack, visited)


def find_basins(data):
    low_points = find_low_points(data)
    basins = []

    for x, y in low_points:
        visited = []
        stack = [(x, y)]
        find_neighbours(data, stack, visited)
        basins.append(len(visited))

    return basins


def calculate_risk(data, low_points):
    return sum(data[y][x] + 1 for x, y in low_points)


def solve_1(data):
    low_points = find_low_points(data)
    return calculate_risk(data, low_points)


def solve_2(data):
    basins = find_basins(data)
    basins.sort(reverse=True)
    return basins[0] * basins[1] * basins[2]


if __name__ == '__main__':
    data = get_data()
    print('Solution 1')
    print(solve_1(data))
    print('\nSolution 2')
    print(solve_2(data))
