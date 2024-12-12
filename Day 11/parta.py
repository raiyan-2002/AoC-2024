filePath = "input.txt"
cache = {}

def dfs(stone, time):
    if time == 0:
        return 1
    if (stone, time) in cache:
        return cache[(stone, time)]
    res = 0
    if int(stone) == 0:
        res += dfs('1', time - 1)
    elif (len(stone) % 2) == 0:
        mid = len(stone) // 2
        s1 = stone[: mid]
        res += dfs(s1, time - 1)
        s2 = stone[mid: ]
        if int(s2) == 0:
            res += dfs('0', time - 1)
        else:
            res += dfs(s2.lstrip('0'), time - 1)
    else:
        res += dfs(str(int(stone) * 2024), time - 1)
    cache[(stone, time)] = res
    return res

stones = []

with open(filePath, 'r') as file:
    for line in file:
        line = line.rstrip('\n')
        stones = line.split(' ')

res = 0
for stone in stones:
    res += dfs(stone, 25)

print(res)