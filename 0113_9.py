n = int(input())
l = list(map(int, input().split()))

max_l = l[0]
min_l = l[0]

for i in l:
    if max_l < i:
        max_l = i

for i in l:
    if min_l > i:
        min_l = i

print(f"{max_l} {min_l}")