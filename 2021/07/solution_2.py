from utils import *


def solve(data):
    return min(
        sum(int((abs(num - x) * (abs(num -x) + 1)) / 2) for num in data)
        for x in range(max(data) + 1)
    )


if __name__ == '__main__':
    data = get_data()
    result = solve(data)
    print(result)
