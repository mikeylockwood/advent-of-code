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

