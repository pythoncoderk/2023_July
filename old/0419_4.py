n = int(input())
l = [int(input()) for i in range(n)]

count = 0
for i in range(n):
    if i + 1 not in l:
        count += 1

print(count)