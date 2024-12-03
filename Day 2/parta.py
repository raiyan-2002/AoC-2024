filePath = "input.txt"

def valid(arr, increasing):

    prev = arr[0]

    for i in range(1, len(arr)):
        curr = arr[i]
        if increasing:
            if curr <= prev:
                return False
        else:
            if curr >= prev:
                return False
        if not (1 <= abs(prev - curr) <= 3):
            return False
        prev = curr

    return True

res = 0

with open(filePath, 'r') as file:
    for line in file:
        strings = line.split(' ')
        ints = [int(string) for string in strings]  
        increasing = ints[0] < ints[-1] # this is true means the sequence should be increasing, false otherwise 
        res += 1 if valid(ints, increasing) else 0

print(res)

        