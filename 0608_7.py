s, t = map(str, input().split())
a, b = map(int, input().split())
u = input()

# print(s, t)
# print(a, b)
# print(u)

d = {s: a, t: b}

d[u] -= 1

print(d[s], d[t])
