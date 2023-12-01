def part1(filePath):
    with open(filePath) as input:
        total = 0
        lines = input.readlines()
        for line in lines:
            mid = len(line) // 2
            first, second = line[:mid], line[mid:]
            firstSet, secondSet = set(), set()
            for c in first:
                firstSet.add(c)
            for c in second:
                secondSet.add(c)
            for val in firstSet:
                if val in secondSet:
                    if val >= 'a':
                        total += ord(val) - ord('a') + 1
                    else:
                        total += ord(val) - ord('A') + 27
        return total
print(part1("input/Day3-Input.txt"))

def part2(filePath):
    with open(filePath) as input:
        total = 0
        lines = input.readlines()
        for i in range(0, len(lines), 3):
            first, second, third = set(), set(), set()
            for c in lines[i].strip():
                first.add(c)
            for c in lines[i + 1].strip():
                second.add(c)
            for c in lines[i + 2].strip():
                third.add(c)
            intersection = first & second & third
            same = list(intersection)[0]
            if same >= 'a':
                total += ord(same) - ord('a') + 1
            else:
                total += ord(same) - ord('A') + 27
        return total

print(part2("input/Day3-Input.txt"))