filePath = "input.txt"
search = "XMAS"

def inRange(y, x, height, width):
    return y >= 0 and y < height and x >= 0 and x < width

def bfs(y, x, grid, dy, dx):

    height = len(grid)
    width = len(grid[0])

    for k in range(4):
        if not inRange(y, x, height, width):
            return 0
        if grid[y][x] != search[k]:
            return 0
        y += dy
        x += dx

    return 1

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
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dy != 0 or dx != 0:
                    res += bfs(y, x, grid, dy, dx)


print(res)