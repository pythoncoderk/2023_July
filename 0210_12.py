n, r = map(int, input().split())
l = [int(input()) for i in range(n)]

# print(n, r)
# print(l)

max_l = max(l)
g = max_l // r
xxx = ""
for i in range(n):
    x = l[i] // r
    for j in range(g):
        if x >= 1:
            xxx += "*"
            x -= 1
        else:
            xxx += "."
    print(f"{i+1}:{xxx}")
    xxx = ""
