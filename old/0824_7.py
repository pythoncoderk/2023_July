x, y, z = map(int, input().split())

ans = 0
while y <= z:
    ans += 1
    z -= y

while x <= z:
    ans += 1
    z -= x

if z != 0:
    ans += z

print(ans)