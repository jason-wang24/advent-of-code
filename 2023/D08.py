import math


def part1(file_path):
    with open(file_path) as input:
        lines = input.readlines()
        instructions = lines[0].strip()
        maps = {}
        for line in lines[2:]:
            key, val = line.strip().split(' = ')
            l, r = val[1:-1].split(', ')
            maps[key] = {"L": l, "R": r}

        steps = 0
        curr = 'AAA'
        while curr != 'ZZZ':
            curr = maps[curr][instructions[steps % len(instructions)]]
            steps += 1
        return steps


print(part1("input/D08.txt"))


def part2(file_path):
    with open(file_path) as input:
        lines = input.readlines()
        instructions = lines[0].strip()
        maps = {}
        start_nodes = []
        for line in lines[2:]:
            key, val = line.strip().split(' = ')
            if key[-1] == 'A':
                start_nodes.append(key)
            l, r = val[1:-1].split(', ')
            maps[key] = {"L": l, "R": r}

        # Observe that, for each start node, the number of steps to reach the next z
        #   is the same for each z. We can just take the LCM due to the cycle
        total_steps = 1
        for node in start_nodes:
            steps = 0
            while node[-1] != 'Z':
                node = maps[node][instructions[steps % len(instructions)]]
                steps += 1
            total_steps = math.lcm(total_steps, steps)
        return total_steps


print(part2("input/D08.txt"))
