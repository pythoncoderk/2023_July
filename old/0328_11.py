n = int(input())
l = list(map(str, input().split()))

# print(n)
# print(l)

l2 = []
x10_count = 0
zero_count = 0
while l:
    if l[0] == "x10":
        x10_count += 1
        l.pop(0)
    elif l[0] == "0":
        zero_count += 1
        l.pop(0)
    else:
        l2.append(int(l[0]))
        l.pop(0)
# print(l2)

max_l = max(l2)
if zero_count >= 1:
    for i in range(len(l2)):
        if l2[i] == max_l:
            l2[i] = 0
            break

if x10_count >= 1:
    print(sum(l2) * 10)
else:
    print(sum(l2))