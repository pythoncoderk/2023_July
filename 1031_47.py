l = list(map(int, input().split()))
z = 0
for i in range(2):
    if l[i] >= 5:
        z += 5
    else:
        z = z + l[i]
print(z)