a, b = map(int, input().split())

chk = False
for i in range(a, b + 1):
    if 100 % i == 0:
        chk = True

print("Yes" if chk else "No")