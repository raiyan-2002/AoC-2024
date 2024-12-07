filePath = "input.txt"

res = []
curr = []
def generate(i, length):
    if i == length:
        res.append(curr[:]) 
        return 
    curr.append(0)
    generate(i + 1, length)
    curr.pop()
    curr.append(1)
    generate(i + 1, length)
    curr.pop()
    curr.append(2)
    generate(i + 1, length)
    curr.pop()

ret = 0

with open(filePath, 'r') as file:
    for line in file:
        line = line.rstrip('\n')
        target, nums = line.split(':')
        target = int(target)
        nums = nums.strip().split(' ')
        nums = [int(num) for num in nums]
        generate(0, len(nums) - 1)
        ops = [[0] + op for op in res]
        res = []

        for op in ops:
            start = 0
            for i in range(len(op)):
                if op[i] == 0:
                    start += nums[i]
                elif op[i] == 1:
                    start *= nums[i]
                else:
                    first = str(start)
                    second = str(nums[i])
                    start = int(first + second)
            
            if start == target:
                ret += target
                break

print(ret)