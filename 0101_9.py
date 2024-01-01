n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
for i in range(n):
    l[i][1] = int(l[i][1])
d = dict(l)
s = list(map(str, input().split()))

# print(n)
# print(d)
# print(s)

target = d[s[0]]
if int(s[1][:2]) - target < 0:
    uk = int(s[1][:2]) - target + 24
else:
    uk = int(s[1][:2]) - target
fainal_m = s[1][-2:]

# print(target)
# print(uk)
# print(fainal_m)

for i in range(n):
    if uk + l[i][1] < 0:
        fainal = uk + l[i][1] + 24
    elif uk + l[i][1] >= 24:
        fainal = uk + l[i][1] -24
    else:
        fainal = uk + l[i][1]
    print(f"{str(fainal).zfill(2)}:{fainal_m}")