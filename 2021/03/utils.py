from pathlib import Path


def parse_data():
    data_file = Path(__file__).with_name('data.txt')

    with data_file.open('r') as f:
        data = f.read()

    return [x for x in data.strip().split('\n')]


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

