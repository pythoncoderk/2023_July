n, l = map(int, input().split())
li = list(map(int, input().split()))

# print(n, l)
# print(li)

count = 0
for i in range(n):
    if li[i] >= l:
        count += 1
print(count)