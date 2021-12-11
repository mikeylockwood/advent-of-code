from utils import *


def solve(data):
    return breed_fish(data, 80)


if __name__ == '__main__':
    data = get_data()
    count = solve(data)
    print(count)
