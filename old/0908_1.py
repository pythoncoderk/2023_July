h, w, n = map(int, input().split())
l = [list(input()) for i in range(h)]
l2 = [list(map(int, input().split())) for i in range(n)]

# print(h, w, n)
# print(l)
# print(l2)

for i in range(n):
    l[l2[i][0]][l2[i][1]] = "#"

for i in l:
    print("".join(i))