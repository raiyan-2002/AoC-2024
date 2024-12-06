filePath = "input.txt"
grid = []

def inRange(y, x, height, width):
    return y >= 0 and y < height and x >= 0 and x < width

with open(filePath, 'r') as file:
    for line in file:
        line = line.rstrip('\n')
        row = []

        for character in line:
            row.append(character)
        grid.append(row)

height = len(grid)
width = len(grid[0])
start = ()

for i in range(height):
    for k in range(width):
        if grid[i][k] == '^':
            start = (i, k)
            break

pos_y, pos_x = start

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
direction = 0
res = 0

for i in range(height):
    for k in range(width):
        if grid[i][k] == '#' or grid[i][k] == '^':
            continue
        visit = set()
        new_obs = (i, k)
        pos_y, pos_x = start
        direction = 0

        while inRange(pos_y, pos_x, height, width):
            if (pos_y, pos_x, direction) in visit:
                res += 1
                break

            dy, dx = directions[direction]
            visit.add((pos_y, pos_x, direction))

            if inRange(pos_y + dy, pos_x + dx, height, width) and grid[pos_y + dy][pos_x + dx] == '.' and (pos_y + dy, pos_x + dx) != new_obs:
                pos_y += dy
                pos_x += dx
            elif (inRange(pos_y + dy, pos_x + dx, height, width) and grid[pos_y + dy][pos_x + dx] == '#') or ((pos_y + dy, pos_x + dx) == new_obs): # obstacle
                direction = (direction + 1) % 4
            else:
                pos_y += dy
                pos_x += dx
print(res)