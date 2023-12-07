from pathlib import Path


HIGH_CARDS = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}


def hand_bid(row):
    hand, bid = row.split()
    return [HIGH_CARDS.get(c) or int(c) for c in hand], int(bid)


def parse(data):
    return map(hand_bid, data.strip().split("\n"))


def get_data():
    data_file = Path(__file__).with_name("data.txt")

    with data_file.open("r") as f:
        data = f.read()

    return parse(data)


HAND_TYPES = {
    (5,): 7,
    (4, 1): 6,
    (3, 2): 5,
    (3, 1, 1): 4,
    (2, 2, 1): 3,
    (2, 1, 1, 1): 2,
    (1, 1, 1, 1, 1): 1,
}


def hand_type(hand):
    cards = set(hand)
    ht = tuple(sorted([hand.count(c) for c in cards], reverse=True))
    return HAND_TYPES[ht]


def replace_jokers(hand):
    if 11 not in hand:
        return hand_type(hand), hand

    cards = set(hand)
    card_dict = {c: hand.count(c) for c in cards}
    joker = card_dict.pop(11)

    if joker == 5:
        return 7, [0, 0, 0, 0, 0]

    most_cards = sorted(
        [k for k in card_dict], key=lambda k: (card_dict[k], k), reverse=True
    )
    top_card = most_cards[0]

    ht = hand_type([top_card if x == 11 else x for x in hand])
    return ht, [0 if x == 11 else x for x in hand]


def get_score(ranks):
    rank = 1
    score = 0
    for x in range(1, 8):
        for _, bet in sorted(ranks[x], key=lambda h: h[0]):
            score += bet * rank
            rank += 1

    return score


def solve_1(data):
    ranks = {x: [] for x in range(1, 8)}

    for row in data:
        hand, _ = row
        ht = hand_type(hand)
        ranks[ht].append(row)

    return get_score(ranks)


def solve_2(data):
    ranks = {x: [] for x in range(1, 8)}

    for hand, bet in data:
        ht, new_hand = replace_jokers(hand)
        ranks[ht].append((new_hand, bet))

    return get_score(ranks)


if __name__ == "__main__":
    data = get_data()
    print("Solution 1")
    print(solve_1(data))
    data = get_data()
    print("\nSolution 2")
    print(solve_2(data))
