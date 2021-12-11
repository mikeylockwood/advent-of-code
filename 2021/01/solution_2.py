from utils import get_data


def solve(data):
    return sum(
        sum(data[x-3:x]) > sum(data[x-4:x-1])
        for x in range(4, len(data) + 1)
    )


if __name__ == '__main__':
    data = get_data()
    result = solve(data)
    print(result)
