from pathlib import Path


def parse(data):
    return [int(x) for x in data.strip().split('\n')]


def get_data():
    data_file = Path(__file__).with_name('data.txt')

    with data_file.open('r') as f:
        data = f.read()

    return parse(data)
