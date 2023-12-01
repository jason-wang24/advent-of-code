def part1(filePath):
    with open(filePath) as input:
        maximum, count = 0, 0
        lines = input.readlines()
        for line in lines:
            if len(line) == 1:
                maximum = max(maximum, count)
                count = 0
            else:
                count += int(line)
        return maximum

print(part1("input/Day1-Input.txt"))

def part2(filePath):
    with open(filePath) as input:
        max3, count = [0] * 3, 0
        lines = input.readlines()
        for line in lines:
            if len(line) == 1:
                if count > max3[-1]:
                    max3[-1] = count
                if count > max3[1]:
                    max3[-1], max3[1] = max3[1], max3[-1]
                if count > max3[0]:
                    max3[0], max3[1] = max3[1], max3[0]
                count = 0
            else:
                count += int(line)
        return sum(max3)

print(part2("input/Day1-Input.txt"))