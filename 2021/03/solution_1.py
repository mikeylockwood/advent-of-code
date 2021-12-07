from utils import *
from statistics import multimode


def solve(data):
    bit_counts = compare_bins(data)
    bin_len = len(max(data))
    most_common = ''.join([common_bit(bit_counts, idx) for idx in range(bin_len)])
    least_common = ''.join([uncommon_bit(bit_counts, idx) for idx in range(bin_len)])
    return int(most_common, 2) * int(least_common, 2)


if __name__ == '__main__':
    data = parse_data()
    result = solve(data)
    print(result)
