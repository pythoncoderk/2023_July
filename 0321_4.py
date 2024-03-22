n = int(input())
l = [int(input()) for i in range(n)]

# print(n)
# print(l)
count = 0
el = 1
for i in range(n):
    count += abs(el - l[i])
    el = l[i]
print(count)
