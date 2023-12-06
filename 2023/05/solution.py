from pathlib import Path


def get_data():
    data_file = Path(__file__).with_name("data.txt")

    with data_file.open("r") as f:
        data = f.read()

    return parse(data)


def parse(data):
    return data.strip().split("\n\n")


def get_mappings(data):
    def get_mapping(i):
        return [
            [int(x) for x in m.split()] for m in data[i].split("\n") if "map" not in m
        ]

    return {
        mapping.split()[0]: get_mapping(i)
        for i, mapping in enumerate(data[1::], start=1)
    }


def get_seeds(data):
    return sorted(int(x) for x in data[0].lstrip("seeds: ").split())


def get_seed_ranges(data):
    seed_line = data[0].lstrip("seeds: ").split()

    seeds = [
        (int(seed_line[i]), int(seed_line[i]) + int(seed_line[i + 1]))
        for i in range(0, len(seed_line), 2)
    ]

    return sorted(seeds, key=lambda x: x[0])


def range_humidity(mappings):
    mapping = sorted(mappings["humidity-to-location"], key=lambda x: x[0])
    min_row = mapping[0]
    min_location, min_location_humidity, rnge = min_row

    if min_location > 0:
        return [(0, min_location, 0)]

    return [(min_location_humidity, min_location_humidity + rnge, 0)]


def min_seed_ranges(mappings, ranges, i=0):
    new_ranges = []

    map_order = [
        "temperature-to-humidity",
        "light-to-temperature",
        "water-to-light",
        "fertilizer-to-water",
        "soil-to-fertilizer",
        "seed-to-soil",
    ]

    mapping = sorted(mappings[map_order[i]], key=lambda x: x[0])

    for x, y, ln in ranges:
        # offset for the location range
        lr = ln

        for child, parent, rng in mapping:
            # if the minimum of the range is larger the mapping range
            if x >= child + rng:
                big_x = True
                continue

            big_x = False

            offset = x - child
            s = parent + offset
            r = rng - offset

            # if the maximum of the range is larger than the mapping range
            if y >= child + rng:
                new_ranges.append((s, s + r, lr))

                lr += r
                x += r
                continue

            pr = y - x
            new_ranges.append((s, s + pr, lr))
            break

        if big_x:
            new_ranges.append((x, y, lr))

    if i == len(map_order) - 1:
        return new_ranges

    return min_seed_ranges(mappings, new_ranges, i + 1)


def solve_1(data):
    seeds = get_seeds(data)
    mappings = get_mappings(data)
    location_ranges = range_humidity(mappings)
    ranges = min_seed_ranges(mappings, location_ranges)

    locations = []
    for x, y, l in ranges:
        for seed in seeds:
            if seed in range(x, y):
                locations.append(l + seed - x)
                break

    return min(locations)


def solve_2(data):
    seed_data = get_seed_ranges(data)
    mappings = get_mappings(data)

    location_ranges = range_humidity(mappings)
    ranges = min_seed_ranges(mappings, location_ranges)

    locations = []
    for x, y, l in ranges:
        for sx, sy in seed_data:
            if sx >= y or sy < x:
                continue

            if sx >= x:
                locations.append(l)
                break

            if sy > x:
                if sx < y:
                    locations.append(l)
                else:
                    locations.append(l + x - sx)
                break

    return min(locations)


if __name__ == "__main__":
    data = get_data()
    print("Solution 1")
    print(solve_1(data))
    print("\nSolution 2")
    print(solve_2(data))
