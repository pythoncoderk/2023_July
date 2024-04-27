n = int(input())
l = [int(input()) for i in range(n)]

# print(n)
# print(l)

count = 0
x = 0
for i in range(n):
    count += abs(l[i] - x)
    x = l[i]

print(count-1)