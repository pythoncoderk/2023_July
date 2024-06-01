nums = [1, 2, 3, 4]

x = 5

n = len(nums)
found = False

for i in range(2 ** n):
    total = 0
    for j in range(n):
        if(i >> j) & 1:
            total += nums[j]
    if total == x:
        found = True
        break
print(found)