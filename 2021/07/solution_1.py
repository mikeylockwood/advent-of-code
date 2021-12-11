from utils import *


def solve(data):
    return min(sum(abs(num - x) for num in data) for x in range(max(data) + 1))


if __name__ == '__main__':
    data = get_data()
    result = solve(data)
    print(result)
