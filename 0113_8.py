l = list(map(int, input().split()))

max_l = l[0]
for i in l:
    if i > max_l:
        max_l = i
min_l = 0
for i in l:
    if i < min_l:
        min_l = i

print(f"{max_l} {min_l}")