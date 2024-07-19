r, c = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(2)]

# print(r, c)
# print(l)

print(l[r-1][c-1])