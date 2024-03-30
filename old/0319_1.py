n = int(input())
l = [int(input()) for i in range(n)]

# print(n)
# print(l)

total = 0
start = 1
for i in range(n):
    total += abs(l[i] - start)
    start = l[i]
print(total)