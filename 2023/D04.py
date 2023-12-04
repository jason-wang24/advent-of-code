def part1(file_path):
    with open(file_path) as input:
        lines = input.readlines()
        total = 0
        for line in lines:
            winning, mine = line.split('|')
            winning = set(winning.split(':')[1].strip().split(' '))
            winning.discard('')
            mine = set(mine.strip().split(' '))
            num_matches = len(winning & mine)
            total += 2 ** (num_matches - 1) if num_matches > 0 else 0
        return total


print(part1("input/D04.txt"))


def part2(file_path):
    with open(file_path) as input:
        lines = input.readlines()
        card_counts = [1] * len(lines)

        for i, line in enumerate(lines, 1):
            winning, mine = line.split('|')
            winning = set(winning.split(':')[1].strip().split(' '))
            winning.discard('')
            mine = set(mine.strip().split(' '))
            for j in range(len(winning & mine)):
                card_counts[i + j] += card_counts[i - 1]
        return sum(card_counts)


print(part2("input/D04.txt"))
