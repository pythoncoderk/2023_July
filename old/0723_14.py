n = int(input())
d = {}
d_l = []
for _ in range(n):
    l = list(map(str, input().split()))
    if l[1] == "give":
        d[l[0]] = int(l[2])
    else:
        d_l.append(l[0])

# print(d)
# print(d_l)

d_2 = sorted(d.items(), key=lambda x: x[1], reverse=True)

# print(d_2)

for _ in range(len(d_2)):
    print(d_2[_][0])

d_l.sort()
for _ in range(len(d_l)):
    print(d_l[_])