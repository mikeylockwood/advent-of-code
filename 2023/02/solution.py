import math
import re

from dataclasses import dataclass
from pathlib import Path


@dataclass
class Colour:
    colour: str
    quantity: int


def parse(data):
    data = re.sub(r'(\n)?Game \d+: ', '\n', data)

    def colour(colour_pick: str):
        quantity, colour = colour_pick.split()
        return Colour(colour, int(quantity))

    return [
        [
            colour(colour_pick)
            for game_round in game.split("; ")
            for colour_pick in game_round.split(", ")
        ]
        for game in data.strip().split('\n')
    ]


def get_data():
    data_file = Path(__file__).with_name('data.txt')

    with data_file.open('r') as f:
        data = f.read()

    return parse(data)


def solve_1(data):
    result = 0

    MAX_VALS = {
        'blue': 14,
        'green': 13,
        'red': 12,
    }

    for num, game in enumerate(data, start=1):
        valid = True

        for colour in game:
            if colour.quantity > MAX_VALS[colour.colour]:
                valid = False
                break

        result += valid and num

    return result


def solve_2(data):
    result = 0
    for game in data:
        min_cubes = {"red": 0, "blue": 0, "green": 0}

        for colour in game:
            min_cubes[colour.colour] = max(
                (min_cubes[colour.colour], colour.quantity))

        result += math.prod(min_cubes.values())

    return result


if __name__ == '__main__':
    data = get_data()
    print('Solution 1')
    print(solve_1(data))
    print('\nSolution 2')
    print(solve_2(data))
