n, x, y, z = map(int, input().split())

# print(n, x, y, z)

if x > y:
    a = x
    b = y

else:
    a = y
    b = x

if b <= z <= a:
    print("Yes")
else:
    print("No")