n, v = map(int, input().split())

l = list(map(int, input().split()))

chk = False
for i in range(n):
    if l[i] == v:
        chk = True

if chk == True:
    print("Yes")
else:
    print("No")