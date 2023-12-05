def part1(file_path):
    with open(file_path) as input:
        lines = input.readlines()

        NUM_MAPS = 7
        maps = []
        specific_map = []
        initial_seeds = list(
            map(int, lines[0].split(':')[1].strip().split(' ')))
        for line in lines[2:]:
            line = line.strip()
            if line == '':
                maps.append(specific_map)
                specific_map = []
                continue
            if line[-1].isdigit():
                specific_map.append(tuple(map(int, line.split(' '))))
        maps.append(specific_map)

        locations = []
        for seed in initial_seeds:
            curr = seed
            for i in range(NUM_MAPS):
                for m in maps[i]:
                    dest, src, length = m
                    if src <= curr <= src + length:
                        curr += dest - src
                        break
            locations.append(curr)

        return min(locations)


print(part1("input/D05.txt"))


def part2(file_path):
    pass


print(part2("input/D05.txt"))
