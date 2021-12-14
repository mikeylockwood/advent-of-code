from pathlib import Path


def parse(data):
    return [(x.split()[0], int(x.split()[1])) for x in data.strip().split('\n')]


def get_data():
    data_file = Path(__file__).with_name('data.txt')

    with data_file.open('r') as f:
        data = f.read()

    return parse(data)


class Submarine:
    horizontal = 0
    depth = 0

    def forward(self, velocity):
        self.horizontal += velocity

    def down(self, velocity):
        self.depth += velocity

    def up(self, velocity):
        self.depth -= velocity

    def move(self, move):
        direction, velocity = move
        getattr(self, direction)(velocity)

    def result(self):
        return self.horizontal * self.depth


def solve_1(data):
    submarine = Submarine()
    for move in data:
        submarine.move(move)

    return submarine.result()


class Sub2(Submarine):
    aim = 0

    def forward(self, velocity):
        self.horizontal += velocity
        self.depth += self.aim * velocity

    def up(self, velocity):
        self.aim -= velocity

    def down(self, velocity):
        self.aim += velocity


def solve_2(data):
    submarine = Sub2()
    for move in data:
        submarine.move(move)

    return submarine.result()


if __name__ == '__main__':
    data = get_data()
    print('Solution 1')
    print(solve_1(data))
    print('\nSolution 2')
    print(solve_2(data))
