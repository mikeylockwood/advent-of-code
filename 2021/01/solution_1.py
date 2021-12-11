from utils import get_data


def solve(data):
    return sum(data[x] > data[x-1] for x in range(1, len(data)))


if __name__ == '__main__':
    data = get_data()
    result = solve(data)
    print(result)
