with open("input/D02.txt") as input:
    lines = input.readlines()
    
    def part1():
        safe = 0
        for line in lines:
            levels = line.split()
            diff = [int(levels[i]) - int(levels[i+1]) for i in range(len(levels) - 1)]
            if (all(d > 0 for d in diff) or all(d < 0 for d in diff)) and max(map(abs, diff)) <= 3:
                safe += 1
        return safe

    def part2():
        def is_safe(levels, can_delete):
            check_deletions = lambda i, count: any(is_safe(levels[:i+di] + levels[i+di+1:], False) for di in range(count))
            diff = [int(levels[i]) - int(levels[i+1]) for i in range(len(levels) - 1)]
            if 0 in diff:
                if not can_delete:
                    return False
                i = diff.index(0)
                return check_deletions(i, 2)
            is_increasing = diff[0] > 0
            if abs(diff[0]) > 3:
                if not can_delete:
                    return False
                return check_deletions(0, 2)
            i = 1
            while i < len(diff):
                if abs(diff[i]) > 3:
                    if not can_delete:
                        return False
                    return check_deletions(i-1, 3)
                if (diff[i] > 0) != is_increasing:
                    if not can_delete:
                        return False
                    return check_deletions(i-1, 3)
                i += 1
            return True                    

        safe = 0
        for line in lines:
            levels = line.split()
            if is_safe(levels, True):
                safe += 1
        return safe
    
    print(part1())
    print(part2())
