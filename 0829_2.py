n = int(input())
l = list(map(int, input().split()))

count = 0
for i in l:
    if i % 3 == 0:
        count += 1

print(count)