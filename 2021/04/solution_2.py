from utils import *


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


def solve(data):
    numbers = get_called_numbers(data)
    cards = get_bingo_cards(data)
    num, card = find_loser(numbers, cards)
    return get_score(num, card)


if __name__ == '__main__':
    data = get_data()
    result = solve(data)
    print(result)
