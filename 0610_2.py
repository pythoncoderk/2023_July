l = list(map(int, input().split()))

total = []
for i in range(3):
    for j in range(3):
        if i != j:
            x = l[i] + l[j]
            total.append(x)

print(min(total))