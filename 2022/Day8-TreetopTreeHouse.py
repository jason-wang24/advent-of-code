def part1(filePath):
    with open(filePath) as input:
        lines = input.readlines()
        visibleCount = 0
        grid = [list(map(int, line.strip())) for line in lines]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                height = grid[row][col]
                if (all(grid[row][i] < height for i in range(col)) or 
                    all(grid[row][i] < height for i in range(col + 1, len(grid[0]))) or 
                    all(grid[i][col] < height for i in range(row)) or 
                    all(grid[i][col] < height for i in range(row + 1, len(grid)))):
                    visibleCount += 1
        return visibleCount

print(part1("input/Day8-Input.txt"))

def part2(filePath):
    with open(filePath) as input:
        lines = input.readlines()
        maxScore = 0
        grid = [list(map(int, line.strip())) for line in lines]
        for row in range(len(grid) - 1):
            for col in range(len(grid[0]) - 1):
                height = grid[row][col]
                left = right = up = down = 0
                for i in range(col - 1, -1, -1):
                    left += 1
                    if grid[row][i] >= height:
                        break
                for i in range(col + 1, len(grid[0])):
                    right += 1
                    if grid[row][i] >= height:
                        break
                for i in range(row - 1, -1, -1):
                    up += 1
                    if grid[i][col] >= height:
                        break
                for i in range(row + 1, len(grid)):
                    down += 1
                    if grid[i][col] >= height:
                        break
                maxScore = max(maxScore, left * right * up * down)
        return maxScore

print(part2("input/Day8-Input.txt"))