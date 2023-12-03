from functools import reduce

def part1(filePath):
    with open(filePath) as input:
        lines = input.readlines()
        table = {}
        # Get numbers into table
        for row, line in enumerate(lines):
            num = ""
            for col, c in enumerate(line):
                if c.isdigit():
                    num += c
                else:
                    if num:
                        pos = (row, col-len(num), col-1) # row, col_start, col_end
                        table[pos] = int(num)
                        num = ""

        total = 0
        for pos, num in table.items():
            row, start, end = pos
            done = False
            for r in range(row-1, row+2):
                if r < 0 or r > len(lines) - 1:
                    continue
                for c in range(start-1, end+2):
                    if c < 0 or c > len(lines[0]) - 2:
                        continue
                    if lines[r][c] != '.' and not lines[r][c].isdigit():
                        total += num
                        done = True
                        break
                if done:
                    break
        return total

print(part1("input/D03.txt"))

def part2(filePath):
    with open(filePath) as input:
        lines = input.readlines()
        table = {}
        # Get numbers into table
        for row, line in enumerate(lines):
            num = ""
            for col, char in enumerate(line):
                if char.isdigit():
                    num += char
                else:
                    if num:
                        for c in range(col-len(num), col):
                            pos = (row, c) # row, col
                            table[pos] = (col-len(num), col-1, int(num)) # col_start, col_end, num
                        num = ""

        total = 0
        for row, line in enumerate(lines):
            for col, char in enumerate(line.strip()):
                if char == "*":
                    bordering = {}
                    for r in range(row-1, row+2):
                        for c in range(col-1, col+2):
                            if (r, c) in table:
                                start, end, num = table[(r, c)]
                                bordering[(r, start, end)] = num
                    if len(bordering) == 2:
                        total += reduce(lambda x, y: x*y, bordering.values())
        return total

print(part2("input/D03.txt"))
