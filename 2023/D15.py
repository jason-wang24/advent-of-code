def hash(string):
    current = 0
    for char in string:
        current += ord(char)
        current *= 17
        current %= 256
    return current


def focusing_power(box_num, slot, focal_length):
    return (box_num + 1) * slot * focal_length


def part1(file_path):
    with open(file_path) as input:
        iv = input.read().split(",")
        checksum = 0
        for step in iv:
            checksum += hash(step.strip())
        return checksum


print(part1("input/D15.txt"))


def part2(file_path):
    with open(file_path) as input:
        iv = input.read().split(",")
        total_power = 0
        boxes = [[] for _ in range(256)]
        for step in iv:
            step = step.strip()
            if step[-1] == '-':
                label = step[:-1]
                checksum = hash(label)
                for i, info in enumerate(boxes[checksum]):
                    if info[0] == label:
                        boxes[checksum].pop(i)
                        break
            else:
                i = step.find('=')
                label, focal_length = step[:i], int(step[i + 1:])
                checksum = hash(label)
                for i, info in enumerate(boxes[checksum]):
                    if info[0] == label:
                        boxes[checksum][i] = (label, focal_length)
                        break
                else:
                    boxes[checksum].append((label, focal_length))

        for box_num, box in enumerate(boxes):
            for slot, info in enumerate(box):
                total_power += focusing_power(box_num, slot + 1, info[1])

        return total_power


print(part2("input/D15.txt"))
