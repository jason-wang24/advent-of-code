from collections import defaultdict, deque

def build_graph(lines):
    graph = defaultdict(list)
    in_edge_count = defaultdict(int)
    for i, line in enumerate(lines):
        if line == '':
            return graph, in_edge_count, i + 1
        left, right = line.split('|')
        graph[left].append(right)
        in_edge_count[right] += 1

def topo_sort(graph, in_edge_count):
    res = {}
    queue = deque([page for page in graph if page not in in_edge_count])
    while queue:
        page = queue.popleft()
        res[page] = len(res)
        if page in graph:
            for pages_after in graph[page]:
                in_edge_count[pages_after] -= 1
                if in_edge_count[pages_after] == 0:
                    queue.append(pages_after)
    return res

with open("input/D05.txt") as input:
    lines = input.read().splitlines()
    graph, in_edge_count, updates_start_i = build_graph(lines)
    def part1():
        total = 0
        for line in lines[updates_start_i:]:
            pages = line.split(',')
            seen = set()
            wrong_order = False
            for page in pages:
                seen.add(page)
                if page in graph:
                    for must_print_after in graph[page]:
                        if must_print_after in seen:
                            wrong_order = True
                            break
                if wrong_order:
                    break
            else:
                total += int(pages[len(pages) // 2])
        return total

    def part2():
        sorted_pages = topo_sort(graph, in_edge_count)
        total = 0
        for line in lines[updates_start_i:]:
            pages = line.split(',')
            seen = set()
            wrong_order = False
            for page in pages:
                seen.add(page)
                if page in graph:
                    for must_print_after in graph[page]:
                        if must_print_after in seen:
                            wrong_order = True
                            break
                if wrong_order:
                    pages.sort(key=lambda p: sorted_pages[p])
                    total += int(pages[len(pages) // 2])
                    break
                    
        return total
    
    print(part1())
    print(part2())
