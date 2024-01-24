n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

for i in range(n):
    l[i][1] = float(l[i][1])

# print(l)

le = [l[i][1] for i in range(n) if l[i][0] == "le"]
ge = [l[i][1] for i in range(n) if l[i][0] == "ge"]

print(f"{max(ge)} {min(le)}")