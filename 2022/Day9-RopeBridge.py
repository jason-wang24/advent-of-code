def part1(filePath):
    with open(filePath) as input:
        lines = input.readlines()
        headPos, tailPos = [0, 0], [0, 0]
        tailVisited = set([(0, 0)])
        for line in lines:
            line = line.strip()
            dir, count = line[0], int(line[2:])
            while count > 0:
                if dir == 'L':
                    headPos[0] -= 1
                elif dir == 'R':
                    headPos[0] += 1
                elif dir == 'U':
                    headPos[1] += 1
                else:
                    headPos[1] -= 1
                xDiff = headPos[0] - tailPos[0]
                yDiff = headPos[1] - tailPos[1]
                if abs(xDiff) == 2:
                    tailPos[0] += 1 if xDiff > 0 else -1
                    tailPos[1] = headPos[1]
                if abs(yDiff) == 2:
                    tailPos[1] += 1 if yDiff > 0 else -1
                    tailPos[0] = headPos[0]
                tailVisited.add((tailPos[0], tailPos[1]))
                count -= 1
        return len(tailVisited)

print(part1("input/Day9-Input.txt"))

def part2(filePath):
    with open(filePath) as input:
        lines = input.readlines()
        knotPos = [[0, 0] for _ in range(10)] # element 0 is head
        tailVisited = set([(0, 0)])
        for line in lines:
            line = line.strip()
            dir, count = line[0], int(line[2:])
            while count > 0:
                if dir == 'L':
                    knotPos[0][0] -= 1
                elif dir == 'R':
                    knotPos[0][0] += 1
                elif dir == 'U':
                    knotPos[0][1] += 1
                else:
                    knotPos[0][1] -= 1                
                for i in range(len(knotPos) - 1):
                    xDiff = knotPos[i][0] - knotPos[i + 1][0]
                    yDiff = knotPos[i][1] - knotPos[i + 1][1]
                    if abs(xDiff) == 2:
                        knotPos[i + 1][0] += 1 if xDiff > 0 else -1
                        knotPos[i + 1][1] = knotPos[i][1]
                    if abs(yDiff) == 2:
                        knotPos[i + 1][1] += 1 if yDiff > 0 else -1
                        knotPos[i + 1][0] = knotPos[i][0]
                tailVisited.add((knotPos[-1][0], knotPos[-1][1]))
                count -= 1
        return len(tailVisited)

print(part2("input/Day9-Input.txt"))