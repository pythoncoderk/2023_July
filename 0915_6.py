n, x = map(int, input().split())
l = list(map(int, input().split()))

# print(n, x)
# print(l)
chk = False
for i in l:
    if i == x:
        chk = True
        break

print("Yes" if chk else "No")