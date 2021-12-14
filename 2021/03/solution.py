from pathlib import Path


def parse(data):
    return data.strip().split('\n')

def get_data():
    data_file = Path(__file__).with_name('data.txt')

    with data_file.open('r') as f:
        data = f.read()

    return parse(data)


def compare_bins(data):
  comparison = [0] * 12
  for binary in data:
     for i, bit in enumerate(binary):
       comparison[i] += int(bit) or -1
  return comparison


def common_bit(bit_counts, idx):
    return '0' if bit_counts[idx] < 0 else '1'


def uncommon_bit(bit_counts, idx):
    return '1' if bit_counts[idx] < 0 else '0'


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


def solve_1(data):
    bit_counts = compare_bins(data)
    bin_len = len(max(data))
    most_common = ''.join([common_bit(bit_counts, idx) for idx in range(bin_len)])
    least_common = ''.join([uncommon_bit(bit_counts, idx) for idx in range(bin_len)])
    return int(most_common, 2) * int(least_common, 2)


def solve_2(data):
    most_common = find_common(data)
    least_common = find_uncommon(data)
    return most_common * least_common


if __name__ == '__main__':
    data = get_data()
    print('Solution 1')
    print(solve_1(data))
    print('\nSolution 2')
    print(solve_2(data))
