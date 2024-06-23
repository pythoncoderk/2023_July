l = [list(map(int, input().split())) for i in range(3)]

# print(l)

total = 0
for i in range(3):
    total += l[i][0] * (l[i][1] / 10)

print(int(total))