n, m, k = map(int, input().split())
l = [int(input())-1 for i in range(m)]

# print(n, m, k)
# print(l)

men = 0
candy = 0
for i in range(n):
    if i in l:
        men += 1
        if men >= k:
            break
    else:
        candy += 1
        men = 0
print(candy)
