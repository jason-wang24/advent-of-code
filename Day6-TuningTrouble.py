def part1(filePath):
    with open(filePath) as input:
        lines = input.readlines()
        window = []
        for i, c in enumerate(lines[0]):
            if i < 3:
                window.append(c)
            else: 
                window.append(c)
                if len(set(window)) == 4:
                    return i + 1
                window.pop(0)

print(part1("input/Day6-Input.txt"))

def part2(filePath):
    with open(filePath) as input:
        lines = input.readlines()
        window = []
        for i, c in enumerate(lines[0]):
            if i < 13:
                window.append(c)
            else: 
                window.append(c)
                if len(set(window)) == 14:
                    return i + 1
                window.pop(0)
                
print(part2("input/Day6-Input.txt"))