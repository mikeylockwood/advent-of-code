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


def find_winner(numbers, cards):
    for num in numbers:
        for card in cards:
            found = find_num(num, card)

            if not found:
                continue

            win = check_win(card, found)

            if not win:
                continue

            return num, card


def find_loser(called_numbers, bingo_cards):
    for num in called_numbers:
        winners = []
        for idx, card in enumerate(bingo_cards):
            found = find_num(num, card)

            if not found:
                continue

            win = check_win(card, found)

            if not win:
                continue

            if len(bingo_cards) == 1:
                return num, card

            winners.append(idx)

        for i in winners[::-1]:
            bingo_cards.pop(i)


def solve_1(data):
    numbers = get_called_numbers(data)
    cards = get_bingo_cards(data)
    num, card = find_winner(numbers, cards)
    return get_score(num, card)


def solve_2(data):
    numbers = get_called_numbers(data)
    cards = get_bingo_cards(data)
    num, card = find_loser(numbers, cards)
    return get_score(num, card)


if __name__ == '__main__':
    data = get_data()
    print('Solution 1')
    print(solve_1(data))
    print('\nSolution 2')
    print(solve_2(data))
