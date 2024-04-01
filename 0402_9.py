n, r = map(int, input().split())

l = [int(input()) for i in range(n)]

# print(n, r)
# print(l)

l2 = []
for i in range(n):
    l2.append(l[i] // r)
# print(l2)
max_l = max(l2)

l3 = []
for i in range(n):
    f_str = ""
    for j in range(l2[i]):
        f_str += "*"
    l3.append(f_str)
# print(l3)

l4 = []
for i in range(n):
    if len(l3[i]) < max_l:
        xxx = l3[i]
        for j in range(max_l - len(l3[i])):
            xxx += "."
        l4.append(xxx)
    else:
        xxx = l3[i]
        l4.append(xxx)
# print(l4)

for i in range(n):
    print(f"{i+1}:{l4[i]}")