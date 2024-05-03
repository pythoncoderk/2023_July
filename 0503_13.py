n, m, k = map(int, input().split())
l = [int(input()) for i in range(m)]

# print(n, m, k)
# print(l)

count = 0
boy = 0
for i in range(1, n + 1):
    if i not in l:
        count += 1
        boy = 0
    else:
        boy += 1
        if boy >= k:
            break
print(count)

