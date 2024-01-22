n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(l)

h = [l[i][2] for i in range(n)]
r = [l[i][3] for i in range(n)]

# print(h)
# print(r)
print(f"{l[0][0]} {l[-1][1]} {max(h)} {min(r)}")