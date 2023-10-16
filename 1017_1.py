n = int(input())
l = list(map(int, input().split()))
x = 0
for i in range(n):
    if l[i] % 2 != 0:
        x = i
        break
    else:
        pass
z = 0
for i in range(x):
    z += l[i]
print(z)