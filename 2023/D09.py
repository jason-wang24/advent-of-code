def part1(file_path):
    with open(file_path) as input:
        lines = input.readlines()

        total = 0
        for line in lines:
            history = line.strip().split(' ')
            histories = [history]
            done = False
            while not done:
                diff = []
                done = True
                for i, num in enumerate(histories[-1][1:], 1):
                    difference = int(num) - int(histories[-1][i - 1])
                    diff.append(difference)
                    if difference != 0:
                        done = False
                histories.append(diff)

            new_val = 0
            for history in histories[::-1]:
                new_val += int(history[-1])
            total += new_val

        return total


print(part1("input/D09.txt"))


def part2(file_path):
    with open(file_path) as input:
        lines = input.readlines()

        total = 0
        for line in lines:
            history = line.strip().split(' ')
            histories = [history]
            done = False
            while not done:
                diff = []
                done = True
                for i, num in enumerate(histories[-1][1:], 1):
                    difference = int(num) - int(histories[-1][i - 1])
                    diff.append(difference)
                    if difference != 0:
                        done = False
                histories.append(diff)

            new_val = 0
            for history in histories[::-1]:
                new_val = int(history[0]) - new_val
            total += new_val

        return total


print(part2("input/D09.txt"))
