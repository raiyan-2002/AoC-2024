import collections

filePath = "input.txt"
grid = []

def inRange(y, x, height, width):
    return y >= 0 and x >= 0 and y < height and x < width

with open(filePath, 'r') as file:
    for line in file:
        line = line.rstrip('\n')
        grid.append([character for character in line])


items = collections.defaultdict(list)
height = len(grid)
width = len(grid[0])

for i in range(height):
    for k in range(width):
        if grid[i][k] != '.':
            items[grid[i][k]].append((i, k))


nodes = set()

for item in items:
    coords = items[item]
    n = len(coords)

    for i in range(n - 1):
        for k in range(i + 1, n):
            dy = coords[i][0] - coords[k][0]
            dx = coords[i][1] - coords[k][1]

            if inRange(coords[k][0] - dy, coords[k][1] - dx, height, width):
                nodes.add((coords[k][0] - dy, coords[k][1] - dx))
            if inRange(coords[i][0] + dy, coords[i][1] + dx, height, width):
                nodes.add((coords[i][0] + dy, coords[i][1] + dx))

print(len(nodes))