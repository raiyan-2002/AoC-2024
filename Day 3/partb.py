import re

filePath = "input.txt"

def compute(line):
    res = 0
    statements = re.finditer(r'mul\((\d+),(\d+)\)', line)  # Finds all digit sequences
    dos = re.finditer(r'do\(\)', line)
    donts = re.finditer(r'don\'t\(\)', line)

    instrs = []

    for do in dos:
        instrs.append((do.end() - 1, True))
    
    for dont in donts:
        instrs.append((dont.end() - 1, False))
    
    instrs.sort()
    i = 0
    for statement in statements:
        index = statement.start()

        while i < len(instrs) and index > instrs[i][0]:
            _, add = instrs[i]
            i += 1
        
        if add:
            res += int(statement.group(1)) * int(statement.group(2))
    return res


with open(filePath, 'r') as file:
    all_text = ""
    for line in file:
        all_text += line
    print(compute("do()" + all_text))

