from utils import *


def solve(data):
    submarine = Submarine()
    for move in data:
        submarine.move(move)

    return submarine.result()


if __name__ == '__main__':
    data = get_data()
    result = solve(data)
    print(result)
