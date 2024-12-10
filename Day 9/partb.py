filePath = "input.txt"
line = ""

with open(filePath, 'r') as file:
    for line in file:
        line = line.rstrip('\n')        


arr = []
id = 0

for i in range(len(line)):
    num = int(line[i])
    if (i % 2 == 0): #even indices
        if num > 0:
            for i in range(num):
                arr.append(id)
            id += 1
    else: # odd indices 
        for i in range(num):
            arr.append('.')

map = []

while i < len(arr):
    curr = arr[i]

    if curr == '.':
        i += 1
        continue
    else:
        start = i
        while i < len(arr) and arr[i] == curr:
            i += 1
        map.append((curr, start, i - start))
    

r = len(map) - 1

for r in range(len(map) - 1, -1, -1):
    id, stop_index, fill = map[r]
    l = 0
    while l < stop_index:
        if arr[l] != '.':
            l += 1
            continue
        start = l
        while l < stop_index and arr[l] == '.':
            l += 1
        length = l - start
        if length >= fill:
            for k in range(fill):
                arr[start + k] = id
            for k in range(fill):
                arr[stop_index + k] = '.'
            break

ret = 0

for i in range(len(arr)):
    if arr[i] == '.':
        continue
    ret += i * int(arr[i])

print(ret)

