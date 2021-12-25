from dataclasses import dataclass, field
from functools import reduce
from pathlib import Path


@dataclass
class Packet:
    v: int = None
    t: int = None
    l: int = None
    subs: list = field(default_factory=list)


def parse(data):
    return ''.join([format(int(x, base=16), '04b') for x in data.strip()])


def get_data():
    data_file = Path(__file__).with_name('data.txt')

    with data_file.open('r') as f:
        data = f.read()

    return parse(data)


def b2(num):
    return int(num, base=2)


def find_packets(trans, idx):
    v, t = map(b2, (trans[idx: idx + 3], trans[idx + 3: idx + 6]))
    idx += 6

    if t == 4:
        lit_val, idx = get_literal(trans, idx)
        return Packet(v, t, lit_val), idx


    l_type = b2(trans[idx])
    idx += 1

    if l_type:
        subs, idx = sub_by_num(trans, idx)
    else:
        subs, idx = sub_by_len(trans, idx)

    return Packet(v, t, subs=subs), idx


def get_literal(trans, idx, val=""):
    val += trans[(idx + 1):(idx + 5)]
    if trans[idx] == "0":
        idx += 5
        return b2(val), idx

    idx += 5
    return get_literal(trans, idx, val)


def sub_by_num(trans, idx):
    num = b2(trans[idx: idx + 11])
    idx += 11
    subs = []

    for _ in range(num):
        sub, idx = find_packets(trans, idx)
        subs.append(sub)

    return subs, idx


def sub_by_len(trans, idx):
    slen = b2(trans[idx:idx + 15])
    idx += 15
    end = idx + slen
    subs = []

    while idx < end:
        sub, idx = find_packets(trans, idx)
        subs.append(sub)

    return subs, idx


def sum_v(packet):
    return sum(map(sum_v, packet.subs)) + packet.v


OPERATORS = {
    0: lambda a, b: a + b,
    1: lambda a, b: a * b,
    2: lambda a, b: a if a < b else b,
    3: lambda a, b: a if a > b else b,
    5: lambda a, b: a > b,
    6: lambda a, b: a < b,
    7: lambda a, b: a == b,
}


def calc_literals(packet):
    if not packet.subs:
        return packet.l

    return reduce(OPERATORS[packet.t], map(calc_literals, packet.subs))


def solve_1(data):
    packet = find_packets(data, 0)[0]
    return sum_v(packet)


def solve_2(data):
    packet = find_packets(data, 0)[0]
    return calc_literals(packet)


if __name__ == '__main__':
    data = get_data()
    print('Solution 1\n', solve_1(data))
    print('\nSolution 2\n', solve_2(data))
