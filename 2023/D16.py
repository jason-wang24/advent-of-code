def part1(file_path, start_beam=(0, 0, 'r')):
    def add_beam():
        move = {'u': (-1, 0), 'd': (1, 0), 'l': (0, -1), 'r': (0, 1)}
        beam = (row + move[direction][0], col + move[direction][1], direction)
        if beam not in visited and 0 <= beam[0] < len(lines[0]) and 0 <= beam[1] < len(lines):
            beams.append(beam)
            visited.add(beam)
            already_energized = (beam[0], beam[1]) in energized
            energized.add((beam[0], beam[1]))
            return 1 if not already_energized else 0
        return 0

    with open(file_path) as input:
        lines = input.read().splitlines()
        num_energized = 1
        beams = [start_beam]  # position, direction
        energized = set(start_beam[:2])
        visited = set(beams)
        while beams:
            row, col, direction = beams.pop()
            if lines[row][col] == ".":
                num_energized += add_beam()
            elif lines[row][col] == "/":
                if direction == 'r':
                    direction = 'u'
                elif direction == 'l':
                    direction = 'd'
                elif direction == 'u':
                    direction = 'r'
                elif direction == 'd':
                    direction = 'l'
                num_energized += add_beam()
            elif lines[row][col] == "\\":
                if direction == 'r':
                    direction = 'd'
                elif direction == 'l':
                    direction = 'u'
                elif direction == 'u':
                    direction = 'l'
                elif direction == 'd':
                    direction = 'r'
                num_energized += add_beam()
            elif lines[row][col] == "|":
                if direction == "u" or direction == "d":
                    num_energized += add_beam()
                else:
                    for direction in ['u', 'd']:
                        num_energized += add_beam()
            elif lines[row][col] == "-":
                if direction == "l" or direction == "r":
                    num_energized += add_beam()
                else:
                    for direction in ['l', 'r']:
                        num_energized += add_beam()

        return num_energized


print(part1("input/D16.txt"))


def part2(file_path):
    with open(file_path) as input:
        lines = input.read().splitlines()

        largest = 0
        for row in range(len(lines)):
            largest = max(largest, part1(file_path, (row, 0, 'r')))
            largest = max(largest, part1(
                file_path, (row, len(lines[0]) - 1, 'l')))
        for col in range(len(lines[0])):
            largest = max(largest, part1(file_path, (0, col, 'd')))
            largest = max(largest, part1(
                file_path, (len(lines) - 1, col, 'u')))
        return largest


print(part2("input/D16.txt"))
