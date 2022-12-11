def part1(filePath):
    with open(filePath) as input:
        lines = input.readlines()
        crateMap = {i + 1: [] for i in range(9)}
        for line in lines:
            if line[0] == '[':
                for i, c in enumerate(line):
                    if c.isalpha():
                        crateMap[i // 4 + 1].append(c)
            elif line[0] == '\n':
                for i in range(1, 10):
                    crateMap[i].reverse()
            elif line[0] == 'm':
                count = int(line[5:line.find('f')])
                start = int(line[line.find('r') + 4:line.find('t')])
                end = int(line[line.find('t') + 3])
                while count > 0:
                    crateMap[end].append(crateMap[start].pop())
                    count -= 1

        topCrates = ''
        for value in crateMap.values():
            topCrates += value[-1]

    return topCrates

print(part1("input/Day5-Input.txt"))

def part2(filePath):
    with open(filePath) as input:
        lines = input.readlines()
        crateMap = {i + 1: [] for i in range(9)}
        for line in lines:
            if line[0] == '[':
                for i, c in enumerate(line):
                    if c.isalpha():
                        crateMap[i // 4 + 1].append(c)
            elif line[0] == '\n':
                for i in range(1, 10):
                    crateMap[i].reverse()
            elif line[0] == 'm':
                count = int(line[5:line.find('f')])
                start = int(line[line.find('r') + 4:line.find('t')])
                end = int(line[line.find('t') + 3])
                crateMap[end] += crateMap[start][-count:]
                crateMap[start] = crateMap[start][:len(crateMap[start]) - count]

        topCrates = ''
        for value in crateMap.values():
            topCrates += value[-1]

    return topCrates

print(part2("input/Day5-Input.txt"))