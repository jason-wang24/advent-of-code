def part1(filePath):
    def compare(left, right):
        i = 0
        while i < len(left) and i < len(right):
            if type(left[i]) == int and type(right[i]) == int:
                if left[i] < right[i]:
                    return True
                if left[i] > right[i]:
                    return False
            elif type(left[i]) == list and type(right[i]) == list:
                if len(left[i]) == 0:
                    return True
                if len(right[i]) == 0:
                    return False
                return compare(left[i], right[i])
            elif type(left[i]) == int and type(right[i]) == list:
                if len(right[i]) == 0:
                    return False
                return compare([left[i]], right[i])
            else:
                return len(left[i]) == 0 or compare(left[i], [right[i]])
            i += 1
        return i != len(left)

    with open(filePath) as input:
        lines = input.readlines()
        i, ans = 0, 0
        while i < len(lines):
            left = lines[i].strip()
            i += 1
            right = lines[i].strip()
            print(left[1:len(left) - 1].split(','), right)
            ans += 0 if compare(list(left[1:len(left) - 1]), list(right[1:len(right) - 1])) else i // 3 + 1
            i += 2
        return ans

print(part1("input/Day13-Input.txt"))

def part2(filePath):
    pass

part2("input/Day13-Input.txt")