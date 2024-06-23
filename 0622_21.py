n = int(input())
l = list(map(int, input().split()))

# print(n)
# print(l)

count = 0
for i in range((n * 2) - 2):
    if l[i] == l[i + 2]:
        count += 1

print(count)