n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    l[i][0] = str(l[i][0])

# print(n)
# print(l)

total = 0
for i in range(n):
    if "5" in l[i][0]:
        total += int(l[i][1] * 0.05)
    elif "3" in l[i][0]:
        total += int(l[i][1] * 0.03)
    else:
        total += int(l[i][1] * 0.01)
print(total)