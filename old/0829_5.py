n = int(input())
l = [input() for _ in range(n)]
m = int(input())
l2 = [input() for _ in range(m)]

# print(n, m)
# print(l)
# print(l2)

for i in range(n):
    for j in range(m):
        if l[i] in l2[j]:
            print("YES")
        else:
            print("NO")

