n = input()

# print(n)

total = 0
count = 1
for i in range(len(n)-1, -1, -1):
    x = int(n[i])
    total += x * count
    count *= 2

print(total)