import collections

filePath = "input.txt"
search = "MAS"

def inRange(y, x, height, width):
    return y >= 0 and y < height and x >= 0 and x < width

all_as = collections.defaultdict(int)

def bfs(y, x, grid, dy, dx):

    init_y = y
    init_x = x
    height = len(grid)
    width = len(grid[0])

    for k in range(3):
        if not inRange(y, x, height, width):
            return
        if grid[y][x] != search[k]:
            return
        y += dy
        x += dx

    all_as[(init_y + dy, init_x + dx)] += 1

grid = []

with open(filePath, 'r') as file:
    for line in file:
        grid.append([character for character in line])
        if grid[-1][-1] == '\n':
            grid[-1].pop()
        

res = 0
height = len(grid)
width = len(grid[0])

for y in range(height):
    for x in range(width):
        for dy in [-1, 1]:
            for dx in [-1, 1]:  
                bfs(y, x, grid, dy, dx)

for pair in all_as:
    if all_as[pair] == 2:
        res += 1

print(res)