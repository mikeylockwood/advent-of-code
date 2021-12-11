from utils import *


class Sub2(Submarine):
    aim = 0

    def forward(self, velocity):
        self.horizontal += velocity
        self.depth += self.aim * velocity

    def up(self, velocity):
        self.aim -= velocity

    def down(self, velocity):
        self.aim += velocity


def solve(data):
    submarine = Sub2()
    for move in data:
        submarine.move(move)

    return submarine.result()


if __name__ == '__main__':
    data = get_data()
    result = solve(data)
    print(result)
