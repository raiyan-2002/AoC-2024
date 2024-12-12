filePath = "input.txt"

grid = []
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def inRange(y, x, height, width):
    return y >= 0 and y < height and x >= 0 and x < width

def bfs(y, x, next, grid):
    height = len(grid)
    width = len(grid[0])

    if next == 9 and grid[y][x] == 9:
        return 1
    elif next == 9:
        return 0
    elif grid[y][x] != next:
        return 0
    
    res = 0

    for dy, dx in directions:
        next_y, next_x = y + dy, x + dx
        if inRange(next_y, next_x, height, width):
            res += bfs(next_y, next_x, next + 1, grid)
    return res

with open(filePath, 'r') as file:
    for line in file:
        line = line.rstrip('\n')
        grid.append([int(c) for c in line])

height = len(grid)
width = len(grid[0])

ret = 0

for i in range(height):
    for k in range(width):
        if grid[i][k] == 0:
            ret += bfs(i, k, 0, grid)

print(ret)
