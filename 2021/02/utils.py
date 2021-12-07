from pathlib import Path


def parse_data():
    data_file = Path(__file__).with_name('data.txt')

    with data_file.open('r') as f:
        data = f.read()

    return [(x.split()[0], int(x.split()[1])) for x in data.strip().split('\n')]


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
