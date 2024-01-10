n, s, d = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
damage = 0
for i in range(n):
    if l[i][0] < s and l[i][1] > d:
        damage += 1

if damage >= 1:
    print("Yes")
else:
    print("No")