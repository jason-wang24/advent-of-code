def part1(filePath):
    with open(filePath) as input:
        lines = input.readlines()
        desiredCycles = set([20, 60, 100, 140, 180, 220])
        cycle, total, x = 0, 0, 1
        for line in lines:
            line = line.strip()
            cycle += 1
            if cycle in desiredCycles:
                total += cycle * x
            if line[0] == 'a':
                cycle += 1
                if cycle in desiredCycles:
                    total += cycle * x
                x += int(line[5:])

        return total

print(part1("input/Day10-Input.txt"))

def part2(filePath):
    pass

print(part2("input/Day10-Input.txt"))