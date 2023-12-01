def part1(filePath):
    shapeScore = {'A': 1, 'B': 2, 'C': 3}
    letterMap = {'X': 'A', 'Y': 'B', 'Z': 'C'}
    with open(filePath) as input:
        score = 0
        lines = input.readlines()
        for line in lines:
            opponent, me = line.split()
            score += shapeScore[letterMap[me]]
            if opponent == letterMap[me]:
                score += 3
            elif (opponent == 'A' and me == 'Y' or 
                  opponent == 'B' and me == 'Z' or 
                  opponent == 'C' and me == 'X'):
                score += 6
        return score

print(part1("input/Day2-Input.txt"))

def part2(filePath):
    shapeScore = {'A': 1, 'B': 2, 'C': 3}
    needToLose = {'B': 'A', 'C': 'B', 'A': 'C'}
    needToWin = {'A': 'B', 'B': 'C', 'C': 'A'}
    with open(filePath) as input:
        score = 0
        lines = input.readlines()
        for line in lines:
            opponent, need = line.split()
            if need == 'X':
                score += shapeScore[needToLose[opponent]]
            elif need == 'Y':
                score += shapeScore[opponent] + 3
            else:
                score += shapeScore[needToWin[opponent]] + 6
        return score

print(part2("input/Day2-Input.txt"))