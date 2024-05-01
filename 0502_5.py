n, r = map(int, input().split())
l = [int(input()) for i in range(n)]
l2 = [(l[i] // r) * "*" for i in range(n)]
# print(n, r)
# print(l)
# print(l2)
l5 = [len(l2[i]) for i in range(n)]
max_l = max(l5)
l3 = []
for i in range(n):
    str_l = l2[i]
    for j in range(max_l):
        if len(str_l) < max_l:
            str_l += "."
    l3.append(str_l)

for i in range(n):
    print(f"{i+1}:{l3[i]}")