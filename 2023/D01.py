def part1(filePath):
    with open(filePath) as input:
        lines = input.readlines()
        total = 0
        for line in lines:
            for c in line:
                if c.isdigit():
                    total += 10 * int(c)
                    break
            for c in line[::-1]:
                if c.isdigit():
                    total += int(c)
                    break
        return total

print(part1("input/D01.txt"))

def part2(filePath):
    wordToNum = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    with open(filePath) as input:
        lines = input.readlines()
        total = 0
        for line in lines:
            earliest = latest = (len(line), None)
            for word, num in wordToNum.items():
                i = line.find(word)
                if -1 < i < earliest[0]:
                    earliest = (i, word)
        
                # latest is finding reverse of word in reverse line
                i = line[::-1].find(word[::-1])
                if -1 < i < latest[0]:
                    latest = (i, word)

                i = line.find(str(num))
                if -1 < i < earliest[0]:
                    earliest = (i, word)

                i = line[::-1].find(str(num))
                if -1 < i < latest[0]:
                    latest = (i, word)
            total += 10 * wordToNum[earliest[1]] + wordToNum[latest[1]]

        return total

print(part2("input/D01.txt"))
