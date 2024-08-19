n = int(input())

d_c = {}
d_m = []
for _ in range(n):
    l = list(map(str, input().split()))
    if l[1] == "give":
        d_c[l[0]] = int(l[2])
    else:
        d_m.append(l[0])

# print(d_c)
# print(d_m)

d_c = list(d_c.items())
c_sort = sorted(d_c, key=lambda x: x[1], reverse=True)

for _ in range(len(c_sort)):
    print(c_sort[_][0])

d_m.sort()
for _ in range(len(d_m)):
    print(d_m[_])

