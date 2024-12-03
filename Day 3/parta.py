import re

filePath = "input.txt"
res = 0

def compute(line):
    res = 0
    statements = re.findall(r'mul\((\d+),(\d+)\)', line)  # Finds all digit sequences
    for x, y in statements:
        res += int(x) * int(y)
    return res

with open(filePath, 'r') as file:
    for line in file:
        res += compute(line)

print(res)
