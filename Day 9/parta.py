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

l = 0
r = len(arr) - 1

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

