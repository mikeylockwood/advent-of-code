from pathlib import Path


def parse(data):
    lines = data.strip().split('\n')

    return [
        [
            [int(x) for x in coord.split(',')]
            for coord in line.split(' -> ')
        ]
        for line in lines
    ]


def get_data():
    data_file = Path(__file__).with_name('data.txt')

    with data_file.open('r') as f:
        data = f.read()

    return parse(data)
