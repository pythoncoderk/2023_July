a, b, x = map(int, input().split())

if a == x:
    print("YES")
    exit()

for i in range(1, b + 1):
    a += 1
    if a == x:
        print("YES")
        exit()

print("NO")