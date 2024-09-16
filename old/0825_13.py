x, y, z = map(int, input().split())

ans = z
for i in range(z // x + 1):
    for j in range(z // y + 1):
        xxx = i * x + j * y
        if z - xxx > 0:
            num_zero = z - xxx
        if ans > i + j + num_zero:
            ans = i + j + num_zero

print(ans)
