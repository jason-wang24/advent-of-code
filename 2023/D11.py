def part1(file_path):
    with open(file_path) as input:
        lines = input.readlines()

        galaxies = []
        empty_row = [1] * len(lines)
        empty_col = [1] * len(lines[0])
        for row, line in enumerate(lines):
            for col, char in enumerate(line):
                if char == '#':
                    empty_row[row] = 0
                    empty_col[col] = 0
                    galaxies.append((row, col))

        total = 0
        for i in range(len(galaxies)):
            for j in range(i + 1, len(galaxies)):
                i_row, i_col = galaxies[i]
                j_row, j_col = galaxies[j]
                total += abs(i_row - j_row) + abs(i_col - j_col)
                # add expansion of universe for empty rows and cols
                for r in range(i_row, j_row):
                    total += empty_row[r]
                for c in range(min(i_col, j_col), max(i_col, j_col)):
                    total += empty_col[c]
        return total


print(part1("input/D11.txt"))


def part2(file_path):
    with open(file_path) as input:
        lines = input.readlines()

        galaxies = []
        empty_row = [1] * len(lines)
        empty_col = [1] * len(lines[0])
        for row, line in enumerate(lines):
            for col, char in enumerate(line):
                if char == '#':
                    empty_row[row] = 0
                    empty_col[col] = 0
                    galaxies.append((row, col))

        total = 0
        for i in range(len(galaxies)):
            for j in range(i + 1, len(galaxies)):
                i_row, i_col = galaxies[i]
                j_row, j_col = galaxies[j]
                total += abs(i_row - j_row) + abs(i_col - j_col)
                # add expansion of universe for empty rows and cols
                for r in range(i_row, j_row):
                    total += empty_row[r] * 999999
                for c in range(min(i_col, j_col), max(i_col, j_col)):
                    total += empty_col[c] * 999999
        return total


print(part2("input/D11.txt"))
