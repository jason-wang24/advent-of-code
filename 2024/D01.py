from collections import defaultdict

with open("input/D01.txt") as input:
    lines = input.readlines()
    
    def part1():
        left, right = [], []
        for line in lines:
            l, r = line.split()
            left.append(int(l))
            right.append(int(r))
        total = 0
        left.sort()
        right.sort()
        for l, r in zip(left, right):
            total += abs(l - r)
        return total

    def part2():
        left, right = [], defaultdict(int)
        for line in lines:
            l, r = line.split()
            left.append(int(l))
            right[int(r)] += 1
        total = 0
        for l in left:
            total += l * right.get(l, 0)
        return total
    
    print(part1())
    print(part2())
