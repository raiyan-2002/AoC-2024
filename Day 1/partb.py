import collections

filePath = "input.txt"
nums1 = []
counts = collections.defaultdict(int)
res = 0


with open(filePath, 'r') as file:
    for line in file:
        item1, item2 = line.split('  ')
        nums1.append(int(item1))
        counts[int(item2)] += 1
        

for num in nums1:
    res += num * counts[num]

print(res)


