import collections

filePath = "input.txt"
graph = collections.defaultdict(set)
lists = []

def valid(arr, graph):
    length = len(arr)

    for i in range(len(arr) - 1, -1, -1):
        curr = arr[i]
        for k in range(i - 1, -1, -1):
            search = arr[k]
            if search in graph[curr]:
                return False
    return True

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
    if valid(arr, graph):
        res += int(arr[mid])

print(res)