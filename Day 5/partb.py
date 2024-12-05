import collections

filePath = "input.txt"
graph = collections.defaultdict(set)
lists = []

def valid(arr, graph):
    for i in range(len(arr) - 1, -1, -1):
        curr = arr[i]
        for k in range(i - 1, -1, -1):
            search = arr[k]
            if search in graph[curr]:
                return False
    return True

def correct(arr, graph): # topo sort
    visited = set()
    stack = []
    nums = set(arr)

    def dfs(node):
        visited.add(node)
        for nei in graph[node]:
            if nei in nums and nei not in visited:
                dfs(nei)
        stack.append(node)

    for vertex in arr:
        if vertex not in visited:
            dfs(vertex)

    return stack[::-1] 

with open(filePath, 'r') as file:
    for line in file:
        line = line.rstrip('\n')
        line = line.strip()
        if '|' in line:
            e1, e2 = line.split('|')
            graph[e1].add(e2)
        elif line != "":
            lists.append(line.split(','))

res = 0

for arr in lists:
    mid = len(arr) // 2
    if not valid(arr, graph):
        real = correct(arr, graph)
        res += int(real[mid])

print(res)