from pathlib import Path


def parse(data):
     return [tuple(map(int, x.strip()[2:].split('..'))) for x in data.strip().split(', ')]


def get_data():
    data_file = Path(__file__).with_name('data.txt')

    with data_file.open('r') as f:
        data = f.read()

    return parse(data)


def check(data, shot):
  min_x, max_x = data[0]
  min_y, max_y = data[1]
  x, y = shot
  return min_x <= x <= max_x and min_y <= y <= max_y


def shoot(data, shot, n):
  x, y = 0, 0
  xv, yv = shot

  for i in range(n):
    x += xv
    y += yv

    xv += 0 - (xv > 0) or xv < 0
    yv -= 1

    if check(data, (x, y)):
      return 1

  return 0


def solve_1(data):
    min_y = min(data[1])
    return (min_y + 1) * min_y // 2


def solve_2(data):
    min_x, max_x = data[0]
    min_y, max_y = data[1]
    count = 0

    for x in range(0, max_x + 1):
        for y in range(min_y, -min_y):
            count += shoot(data, (x , y), 2 * (-min_y))
    return count


if __name__ == '__main__':
    data = get_data()
    print('Solution 1\n', solve_1(data))
    print('\nSolution 2\n', solve_2(data))
