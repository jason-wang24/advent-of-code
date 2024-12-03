import re

with open("input/D03.txt") as input:
    data = input.read()
    
    def part1():
        total = 0
        pattern = r"mul\(\d{1,3},\d{1,3}\)"
        matches = re.findall(pattern, data)
        for match in matches:
            first, second = match.split(',')
            total += int(first[4:]) * int(second[:-1])

        return total

    def part2():
        total = 0
        pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
        matches = re.findall(pattern, data)
        i = 0
        while i < len(matches):
            match = matches[i]
            if match == "don't()":
                try:
                    i += matches[i:].index("do()")
                except ValueError:
                    return total
            if match[0] == 'm':
                first, second = match.split(',')
                total += int(first[4:]) * int(second[:-1])
            i += 1
    
        return total
    
    print(part1())
    print(part2())
