from collections import deque

def solve(days, lst):
    if days == 0:
        return len(lst)

    babs = sum(f == 0 for f in lst)
    fish = [6 if f == 0 else f - 1 for f in lst]
    fish += [8] * babs
    days -= 1

    return solve(days, fish)


if __name__ == '__main__':
    data = get_data()
    print(solve(18, data))
    print(solve(256, data))
