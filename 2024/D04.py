import re

with open("input/D04.txt") as input:
    lines = input.read().splitlines()

    def part1():
        total = 0
        pattern = r'(?=(XMAS|SAMX))'
        
        # horizontal
        for line in lines:
            total += len(re.findall(pattern, line))

        # vertical
        rotated = map(''.join, zip(*lines))
        for line in rotated:
            total += len(re.findall(pattern, line))

        # negative slope diagonal
        m, n = len(lines), len(lines[0])
        for r in range(m - 3):
            for c in range(n - 3):
                word = ''.join([lines[r+i][c+i] for i in range(4)])
                if word == "XMAS" or word == "SAMX":
                    total += 1

        # positive slope diagonal
        for r in range(m - 3):
            for c in range(3, n):
                word = ''.join([lines[r+i][c-i] for i in range(4)])
                if word == "XMAS" or word == "SAMX":
                    total += 1
        
        return total

    def part2():
        total = 0
        m, n = len(lines), len(lines[0])
        for r in range(m - 2):
            for c in range(n - 2):
                neg_slope_diag = ''.join([lines[r+i][c+i] for i in range(3)])
                pos_slope_diag = ''.join([lines[r+i][c+2-i] for i in range(3)])
                if neg_slope_diag in ('MAS', 'SAM') and pos_slope_diag in ('MAS', 'SAM'):
                    total += 1
        return total
    
    print(part1())
    print(part2())
