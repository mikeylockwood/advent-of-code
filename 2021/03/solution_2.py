from utils import *


def filter_bins(data, idx, bit):
  return [x for x in data if x[idx] == bit]


def find_common(data, idx=0):
    if len(data) == 1:
        return int(data[0], 2)

    bit_counts = compare_bins(data)

    if idx == len(max(data)) - 1:
        bin_str = ''.join([common_bit(bit_counts, i) for i in range(idx + 1)])
        return int(bin_str, 2)

    bit = common_bit(bit_counts, idx)
    data = filter_bins(data, idx, bit)

    return find_common(data, idx + 1)


def find_uncommon(data, idx=0):
    if len(data) == 1:
        return int(data[0], 2)

    bit_counts = compare_bins(data)

    if idx == len(max(data)) - 1:
        bin_str = ''.join([uncommon_bit(bit_counts, i) for i in range(idx + 1)])
        return int(bin_str, 2)

    bit = uncommon_bit(bit_counts, idx)
    data = filter_bins(data, idx, bit)

    return find_uncommon(data, idx + 1)


def solve(data):
    most_common = find_common(data)
    least_common = find_uncommon(data)
    return most_common * least_common


if __name__ == '__main__':
    data = get_data()
    result = solve(data)
    print(result)
