n = int(input())
l = list(map(str, input().split()))
l2 = [l[i] if l[i] == "x10" else int(l[i]) for i in range(n)]

# print(n)
# print(l2)

max_l = 0
for i in range(n):
    if l2[i] != "x10":
        if max_l < l2[i]:
            max_l = l2[i]

x10_count = 0
for i in range(n):
    if l2[i] == "x10":
        x10_count += 1

zero_count = 0
for i in range(n):
    if l2[i] == 0:
        zero_count += 1

if zero_count >= 1:
    for i in range(n):
        if l2[i] == max_l:
            l2[i] = 0
            break

f_count = 0
if x10_count >= 1:
    for i in range(n):
        if l2[i] != "x10":
            f_count += l2[i]

    print(f_count * 10)

else:
    for i in range(n):
        if l2[i] != "x10":
            f_count += l2[i]
    print(f_count)