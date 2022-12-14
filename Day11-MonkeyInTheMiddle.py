def part1(filePath):
    with open(filePath) as input:
        monkies = []
        lines = input.readlines()
        i = 1
        while i < len(lines):
            newMonkey = {'inspectCount': 0}
            line = lines[i].strip()
            newMonkey['items'] = [int(i) for i in line[16:].split(', ')]
            i += 1
            line = lines[i].strip()
            newMonkey['op'] = eval(f'lambda old:{line[17:]}')
            i += 1
            test = lines[i].strip()
            i += 1
            true = lines[i].strip()
            i += 1
            false = lines[i].strip()
            newMonkey['test'] = (int(test[19:]), int(true[25:]), int(false[26:]))
            monkies.append(newMonkey)
            i += 3

        for _ in range(20):
            for monkey in monkies:
                monkey['inspectCount'] += len(monkey['items'])
                for item in monkey['items']:
                    item = monkey['op'](item) // 3
                    if item % monkey['test'][0] == 0:
                        monkies[monkey['test'][1]]['items'].append(item)
                    else:
                        monkies[monkey['test'][2]]['items'].append(item)
                monkey['items'] = []

        monkies.sort(key=lambda x: x['inspectCount'], reverse=True)
        return monkies[0]['inspectCount'] * monkies[1]['inspectCount']

print(part1("input/Day11-Input.txt"))

def part2(filePath):
    with open(filePath) as input:
        monkies = []
        lines = input.readlines()
        i = 1
        while i < len(lines):
            newMonkey = {'inspectCount': 0}
            line = lines[i].strip()
            newMonkey['items'] = [int(i) for i in line[16:].split(', ')]
            i += 1
            line = lines[i].strip()
            newMonkey['op'] = eval(f'lambda old:{line[17:]}')
            i += 1
            test = lines[i].strip()
            i += 1
            true = lines[i].strip()
            i += 1
            false = lines[i].strip()
            newMonkey['test'] = (int(test[19:]), int(true[25:]), int(false[26:]))
            monkies.append(newMonkey)
            i += 3

        productOfTests = 1
        for monkey in monkies:
            productOfTests *= monkey['test'][0]

        for _ in range(10000):
            for monkey in monkies:
                monkey['inspectCount'] += len(monkey['items'])
                for item in monkey['items']:
                    item = monkey['op'](item) % productOfTests
                    if item % monkey['test'][0] == 0:
                        monkies[monkey['test'][1]]['items'].append(item)
                    else:
                        monkies[monkey['test'][2]]['items'].append(item)
                monkey['items'] = []

        monkies.sort(key=lambda x: x['inspectCount'], reverse=True)
        return monkies[0]['inspectCount'] * monkies[1]['inspectCount']

print(part2("input/Day11-Input.txt"))