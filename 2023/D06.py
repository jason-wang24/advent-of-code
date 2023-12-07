def part1(file_path):
    with open(file_path) as input:
        lines = input.readlines()
        raw_input = []
        for line in lines:
            num = ''
            for char in line.split(':')[1].strip():
                if char.isdigit():
                    num += char
                else:
                    if num:
                        raw_input.append(int(num))
                        num = ''
            if num:
                raw_input.append(int(num))
        data = zip(raw_input[:len(raw_input) // 2],
                   raw_input[len(raw_input) // 2:])

        total = 1
        for time, record in data:
            margin = 0
            for hold in range(1, time):
                distance = hold * (time - hold)
                if distance > record:
                    margin += 1
            total *= margin
        return total


print(part1("input/D06.txt"))


def part2(file_path):
    with open(file_path) as input:
        lines = input.readlines()
        data = [0, 0]
        for i, line in enumerate(lines):
            num = ''
            for char in line.split(':')[1].strip():
                if char.isdigit():
                    num += char
            data[i] = int(num)

        time, record = data
        # use the property that numbers closer together have greater product
        # binary search from 1 to time-1
        left, right = 1, time - 1
        while left <= right:
            mid = (left + right) // 2
            if mid * (time - mid) > record:
                # check for shorter hold times
                right = mid - 1
            else:
                # check for longer hold times
                left = mid + 1

        # left now contains the minimum hold time (I think? or is it right + 1)
        # we can have hold times from [left, time-left] inclusive
        margin = (time-left) - left + 1
        return margin


print(part2("input/D06.txt"))
