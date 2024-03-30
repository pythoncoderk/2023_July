n = int(input())
l = list(map(str, input().split()))
for i in range(n):
    if l[i] != 'x10':
        l[i] = int(l[i])
x_count = 0
for i in range(n):
    if l[i] == "x10":
        x_count += 1
        l[i] = 999

max_l = 0
for i in range(n):
    if l[i] > max_l and l[i] != 999:
        max_l = l[i]

zero_l = 0
if l.count(0) >= 1:
    zero_l += 1

# print(zero_l)
# print(max_l)
# print(x_count)
# print(n)
# print(l)

if zero_l >= 1:
    for i in range(n):
        if l[i] == max_l and l[i] != 999:
            l[i] = 0
            break

for i in range(n):
    if l[i] == 999:
        l[i] = 0

total = sum(l)

if x_count >= 1:
    print(total * 10)
else:
    print(total)
