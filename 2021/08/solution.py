from pathlib import Path


def parse(data):
    return [
        [[z for z in y.split()] for y in x.split(' | ')]
        for x in data.replace('|\n', '| ').strip().split('\n')
    ]


def get_data():
    data_file = Path(__file__).with_name('data.txt')

    with data_file.open('r') as f:
        data = f.read()

    return parse(data)


knowns = [1, 4, 7, 8]

lens_to_nums = {
    2: 1,
    4: 4,
    3: 7,
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: 8,
}

def solve_1(data):
    lens = [2, 3, 4, 7]

    return sum(1 for x in data for y in x[1] if lens_to_nums[len(y)] in knowns)


def solve_2(data):
    output = []
    for i, o in data:
        lens_to_strs = {k: [] for k in lens_to_nums.keys()}
        strs_to_nums = {}
        nums_to_strs = {}
        for x in i:
            k = len(x)
            if x not in lens_to_strs[k]:
                lens_to_strs[k].append(x)

        for k, v in lens_to_nums.items():
            if type(v) == int:
                num_str = lens_to_strs[k][0]
                strs_to_nums[num_str] = v
                nums_to_strs[v] = num_str

        for x in lens_to_strs[6]:
            if sum(x.count(l) for l in nums_to_strs[1]) == 1:
                strs_to_nums[x] = 6
                nums_to_strs[6] = x
            elif sum(x.count(l) for l in nums_to_strs[4]) == 4:
                strs_to_nums[x] = 9
                nums_to_strs[9] = x
            else:
                strs_to_nums[x] = 0
                nums_to_strs[0] = x

        for x in lens_to_strs[5]:
            if sum(x.count(l) for l in nums_to_strs[6]) == 5:
                strs_to_nums[x] = 5
                nums_to_strs[5] = x
            elif sum(x.count(l) for l in nums_to_strs[1]) == 1:
                strs_to_nums[x] = 2
                nums_to_strs[2] = x
            else:
                strs_to_nums[x] = 3
                nums_to_strs[3] = x

        output.append(''.join([
                str(strs_to_nums[x])
                for s in o
                for x in strs_to_nums
                if len(x) == len(s)
                and sum(s.count(i) for i in x) == len(x)
            ]))

    return sum(int(x) for x in output)


if __name__ == '__main__':
    data = get_data()
    print('Solution 1')
    print(solve_1(data))
    print('\nSolution 2')
    print(solve_2(data))
