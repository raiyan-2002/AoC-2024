import collections

filePath = "test.txt"
line = ""

with open(filePath, 'r') as file:
    for line in file:
        line = line.rstrip('\n')        


arr = []
id = 0
map = collections.defaultdict(list)

for i in range(len(line)):
    num = int(line[i])

    if (i % 2 == 0): #even indices
        if num > 0:
            for i in range(num):
                arr.append(id)
            map[id] = num
            id += 1
    else: # odd indices 
        for i in range(num):
            arr.append('.')

print(''.join([str(c) for c in arr]))
print(map)
l = 0
r = 0

while r < len(line):
    while r < len(line) and line[r] != '.':
        r += 1
    end = r
    while r < len(line) and line[end] == '.':
        end += 1
    length = end - r
    search = id

    while search >= 0:
        if map[search] > 0 and map[search] <= length:
            for i in range(map[search]):
                line[r + i] = search
            search -= 1
            break
        search -= 1
    

    r = end 
            

for r in range(len(line)):


search = id 

while map[search]


while l < r and r >= 0:
    if arr[r] == '.':
        r -= 1
        continue
    while l < r and arr[l] != '.':
        l += 1
    arr[l], arr[r] = arr[r], arr[l]
    r -= 1

ret = 0

for i in range(len(arr)):
    if arr[i] == '.':
        break
    ret += i * arr[i]

print(ret)

