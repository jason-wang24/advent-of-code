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
    with open(filePath) as input:
        lines = input.readlines()
        x = 1
        o = []
        for line in lines:
            line = line.strip()
            o.append(x)
            if line[0] == 'a':
                v = int(line.split()[1])
                o.append(x)
                x += v

        for i in range(0, len(o), 40):
            for j in range(40):
                print(end = "#" if abs(o[i + j] - j) <= 1 else " ")
            print()

part2("input/Day10-Input.txt")