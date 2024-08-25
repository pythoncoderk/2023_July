x, y, z = map(int, input().split())

# print(x, y, z)
ans = z
for i in range((z // x) + 1):
    for j in range((z // y) + 1):
        xxx = i * x + j * y
        if z >= xxx:
            num_zero = z - xxx
            ans = min(ans, num_zero + i + j)

print(ans)



