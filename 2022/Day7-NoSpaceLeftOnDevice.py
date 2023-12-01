def part1(filePath):
    with open(filePath) as input:
        lines = input.readlines()
        contents = cwd = {}
        dirStack = []
        for line in lines:
            line = line.strip()
            if line[0] == '$':
                if line[2] == 'c':
                    dir = line[5:]
                    if dir == '/':
                        cwd = contents
                        dirStack = []
                    elif dir == '..':
                        cwd = dirStack.pop()
                    else:
                        if dir not in cwd:
                            cwd[dir] = {}
                        dirStack.append(cwd)
                        cwd = cwd[dir]
            else:
                left, right = line.split()
                if left == 'dir':
                    if right not in cwd:
                        cwd[right] = {}
                else:
                    cwd[right] = int(left)

    def recurse(dir):
        if type(dir) == int:
            return (dir, 0)
        size, accumulator = 0, 0
        for child in dir.values():
            childSize, childAccumulator = recurse(child)
            size += childSize
            accumulator += childAccumulator
        if size <= 100000:
            accumulator += size
        return (size, accumulator)

    return recurse(contents)[1]

print(part1("input/Day7-Input.txt"))

def part2(filePath):
    with open(filePath) as input:
        lines = input.readlines()
        contents = cwd = {}
        dirStack = []
        for line in lines:
            line = line.strip()
            if line[0] == '$':
                if line[2] == 'c':
                    dir = line[5:]
                    if dir == '/':
                        cwd = contents
                        dirStack = []
                    elif dir == '..':
                        cwd = dirStack.pop()
                    else:
                        if dir not in cwd:
                            cwd[dir] = {}
                        dirStack.append(cwd)
                        cwd = cwd[dir]
            else:
                left, right = line.split()
                if left == 'dir':
                    if right not in cwd:
                        cwd[right] = {}
                else:
                    cwd[right] = int(left)

    def getSize(dir):
        if type(dir) == int:
            return dir
        return sum(map(getSize, dir.values()))

    minDeleteSize = getSize(contents) - 40000000
    
    def recurse(dir):
        size = getSize(dir)
        res = size if size >= minDeleteSize else float('inf')
        for child in dir.values():
            # skip files
            if type(child) != int:
                childMinSize = recurse(child)
                res = min(res, childMinSize)
        return res

    return recurse(contents)
                
print(part2("input/Day7-Input.txt"))