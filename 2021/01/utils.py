from pathlib import Path


def parse_data():
    data_file = Path(__file__).with_name('data.txt')

    with data_file.open('r') as f:
        data = f.read()

    return [int(x) for x in data.strip().split('\n')]
