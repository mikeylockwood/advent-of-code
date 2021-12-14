from collections import defaultdict
from pathlib import Path


def parse(data):
    return [row.split('-') for row in data.strip().split()]


def get_data():
    data_file = Path(__file__).with_name('data.txt')

    with data_file.open('r') as f:
        data = f.read()

    return parse(data)


def find_routes(data):
    routes = defaultdict(list)
    for route in data:
        for a, b in zip(route, reversed(route)):
            if b == 'start':
                continue
            routes[a].append(b)
    routes.pop('end')
    return routes


def navigate(routes, path=['start'], v=False):
    count = 0
    for cave in routes[path[-1]]:
        if cave.islower() and cave in path:
            if not v:
                count += navigate(routes, path + [cave], v=True)
            continue

        count += 1 if cave == 'end' else navigate(routes, path + [cave], v)

    return count


def solve_1(data):
    routes = find_routes(data)
    return navigate(routes, v=True)


def solve_2(data):
    routes = find_routes(data)
    count = navigate(routes)
    return count


if __name__ == '__main__':
    data = get_data()
    print('Solution 1')
    print(solve_1(data))
    print('\nSolution 2')
    print(solve_2(data))
