h, w = map(int, input().split())
l = [list(input()) for i in range(h)]
y, x = map(int, input().split())

# print(h, w)
# print(l)
# print(y, x)

if l[y][x] == ".":
    l[y][x] = "#"
else:
    l[y][x] = "."

for i in range(h):
    print("".join(l[i]))