from utils import *


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

def solve(data):
    numbers = get_called_numbers(data)
    cards = get_bingo_cards(data)
    num, card = find_winner(numbers, cards)
    return get_score(num, card)


if __name__ == '__main__':
    data = get_data()
    result = solve(data)
    print(result)
