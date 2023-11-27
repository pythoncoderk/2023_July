n = int(input())
l = list(map(str, input().split()))
# print(n)
# print(l)
x10 = 0
for i in range(n):
    if l[i] == "x10":
        x10 += 1
    else:
        l[i] = int(l[i])
# print(l)
ten = 0
while "x10" in l:
    if l[ten] == "x10":
        l.pop(ten)
        ten += 1
    else:
        ten += 1
zero = 0
while 0 in l:
    if l[zero] == 0:
        l.pop(zero)
        l_max = max(l)
        max_index = l.index(l_max)
        l[max_index] = -999
        zero += 1
    else:
        zero += 1
for i in range(len(l)):
    if l[i] == -999:
        l[i] = 0
# print(l)
# print(x10)
if x10 != 0:
    print(sum(l) * (x10 * 10))
else:
    print(sum(l))