n = int(input())

l = [list(map(str, input().split())) for i in range(n)]
l = [[l[i][0], float(l[i][1])] for i in range(n)]

# print(n)
# print(l)

ge = [l[i][1] for i in range(n) if l[i][0] == "ge"]
le = [l[i][1] for i in range(n) if l[i][0] == "le"]

# print(ge)
# print(le)

print(f"{max(ge)} {min(le)}")