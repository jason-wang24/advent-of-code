def part1(filePath):
    with open(filePath) as input:
        lines = input.readlines()
        count = 0
        for line in lines:
            pair = line.strip().split(',')
            e1, e2 = pair[0].split('-'), pair[1].split('-')
            e1low, e1high = int(e1[0]), int(e1[1])
            e2low, e2high = int(e2[0]), int(e2[1])
            if ((e1low <= e2low and e1high >= e2high) or 
                (e2low <= e1low and e2high >= e1high)):
                count += 1
        return count

print(part1("Day4-Input.txt"))

def part2(filePath):
    with open(filePath) as input:
        lines = input.readlines()
        count = 0
        for line in lines:
            pair = line.strip().split(',')
            e1, e2 = pair[0].split('-'), pair[1].split('-')
            e1low, e1high = int(e1[0]), int(e1[1])
            e2low, e2high = int(e2[0]), int(e2[1])
            if ((e1low <= e2low and e1high >= e2low) or
                (e2low <= e1low and e2high >= e1low)):
                count += 1
        return count

print(part2("Day4-Input.txt"))