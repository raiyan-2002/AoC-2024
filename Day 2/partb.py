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
        
        if valid(ints, increasing):
            res += 1
        else:
            for i in range(len(ints)):
                arr = ints[: i] + ints[i + 1: ]
                increasing = arr[0] < arr[-1]
                if valid(arr, increasing):
                    res += 1
                    breakfilePath = "input.txt"
print(res)

        