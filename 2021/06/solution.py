from pathlib import Path


def parse(data):
    fish = [int(x) for x in data.strip().split(',')]
    return {x: fish.count(x) for x in range(1, 9)}


def get_data():
    data_file = Path(__file__).with_name('data.txt')

    with data_file.open('r') as f:
        data = f.read()

    return parse(data)


def breed_fish(fish, days):
    if days == 0:
        return sum(fish.values())

    days -= 1

    new_fish = {
        k - 1 if k > 0 else 8: v
        for k, v in fish.items()
    }

    if new_fish.get(6):
        if new_fish.get(8):
            new_fish[6] += new_fish[8]
    elif new_fish.get(8):
        new_fish[6] = new_fish[8]

    return breed_fish(new_fish, days)


def solve_1(data):
    return breed_fish(data, 80)


def solve_2(data):
    return breed_fish(data, 256)


if __name__ == '__main__':
    data = get_data()
    print('Solution 1')
    print(solve_1(data))
    print('\nSolution 2')
    print(solve_2(data))
