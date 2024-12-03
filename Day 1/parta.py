filePath = "input.txt"
nums1 = []
nums2 = []
res = 0


with open(filePath, 'r') as file:
    for line in file:
        item1, item2 = line.split('  ')
        nums1.append(int(item1))
        nums2.append(int(item2))

nums1.sort()
nums2.sort()

for i in range(1000):
    res += abs(nums1[i] - nums2[i])

print(res)


