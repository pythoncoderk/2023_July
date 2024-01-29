n = int(input())
l = list(map(str, input().split()))
l2 = [101 if l[i] == "x10" else int(l[i]) for i in range(n)]
# print(l2)
x10 = False
zero = False
pop_count1 = 0
pop_count2 = 0
for i in range(len(l2)):
    if l2[i] == 101:
        x10 = True
        pop_count1 = i
if x10:
    l2.pop(pop_count1)
for i in range(len(l2)):
    if l2[i] == 0:
        zero = True
        pop_count2 = i
if zero:
    l2.pop(pop_count2)
# print(l2)
max_l = max(l2)
if zero:
    for i in range(len(l2)):
        if l2[i] == max_l:
            l2[i] = 0
            break

if x10:
    print(sum(l2) * 10)
else:
    print(sum(l2))