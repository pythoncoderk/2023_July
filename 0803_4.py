h, w, r, c = map(int, input().split())
l = [list(input()) for i in range(h)]

# print(h, w, r, c)
# print(l)

if l[r-1][c-1] == "#":
    print("Yes")
else:
    print("No")