from pathlib import Path


def parse(data):
    return data.replace('  ', ' ').strip().split('\n\n')


def get_data():
    data_file = Path(__file__).with_name('data.txt')

    with data_file.open('r') as f:
        data = f.read()

    return parse(data)


def get_called_numbers(data):
    return [int(x) for x in data[0].split(',')]


def get_bingo_cards(data):
    return [
        [[int(x) for x in row.split()] for row in board.split('\n')]
        for board in data[1:]
    ]


def find_num(num, card):
    for y, row in enumerate(card):
        if num not in row:
            continue

        x = row.index(num)
        row[x] = False
        return (x, y)


def check_win(card, found):
    x, y = found
    win = [False] * 5

    return (
        [card[yy][x] for yy in range(5)] == win
        or [card[y][xx] for xx in range(5)] == win
    )


def get_score(num, card):
    return num * sum(sum(row) for row in card)
