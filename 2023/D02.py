from functools import reduce

def part1(filePath):
    colorMax = {"red": 12, "green": 13, "blue": 14}
    with open(filePath) as input:
        lines = input.readlines()
        IDSum = 0
        for line in lines:
            ID, data = line.strip().split(':')
            ID = int(ID.split(' ')[1])
            games = data.split(';')
            possible = True
            for game in games:
                colors = game.split(',')
                for info in colors:
                    amount, color = info.strip().split(' ')
                    if colorMax[color] < int(amount):
                        possible = False
            if possible:
                IDSum += ID
        return IDSum

print(part1("input/D02.txt"))

def part2(filePath):
    with open(filePath) as input:
        lines = input.readlines()
        powerSum = 0
        for line in lines:
            data = line.split(':')[1].strip()
            games = data.split(';')

            maxPerColor = {"red": 0, "green": 0, "blue": 0}
            for game in games:
                colors = game.split(',')
                for info in colors:
                    amount, color = info.strip().split(' ')
                    maxPerColor[color] = max(maxPerColor[color], int(amount))
            power = reduce(lambda x, y: x*y, maxPerColor.values())
            powerSum += power
        return powerSum

print(part2("input/D02.txt"))
