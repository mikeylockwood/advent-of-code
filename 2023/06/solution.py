from pathlib import Path
import re
import math


def parse(data):
    data = re.sub(r"(\n)?(Time|Distance):\s+", "\n", data)
    return zip(*[[int(y) for y in x.split() if y] for x in data.strip().split("\n")])


def get_data():
    data_file = Path(__file__).with_name("data.txt")

    with data_file.open("r") as f:
        data = f.read()

    return parse(data)


def find_wins(t, d):
    return sum(1 for x in range(1, t + 1) if (t - x) * x > d)


def solve_1(data):
    return math.prod(find_wins(*td) for td in data)


def solve_2(data):
    data = list(data)
    t = int("".join(str(x[0]) for x in data))
    d = int("".join(str(x[1]) for x in data))
    return find_wins(t, d)


if __name__ == "__main__":
    data = get_data()
    print("Solution 1")
    print(solve_1(data))
    data = get_data()
    print("\nSolution 2")
    print(solve_2(data))
