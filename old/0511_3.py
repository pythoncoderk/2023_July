l = list(map(int, input().split()))

max_p = 0
for i in range(3):
    for j in range(3):
        if i != j:
            if max_p < l[i] + l[j]:
                max_p = l[i] + l[j]
print(max_p)
