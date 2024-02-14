n = int(input())
l = list(map(int, input().split()))

# print(n)
# print(l)
l2 = l[::]
g = max(l)

for i in range(n):
    if l2[i] == g:
        l2[i] = -1
s = max(l2)
s_count = l2.count(-1)

if s_count == 1:
    for i in range(n):
        if l2[i] == s:
            l2[i] = -2
b = max(l2)
b_count = l2.count(-2)

if b_count == 1:
    for i in range(n):
        if l2[i] == b:
            l2[i] = -3
# print(l2)

for i in range(n):
    if l2[i] == -1:
        print("G")
    elif l2[i] == -2:
        print("S")
    elif l2[i] == -3:
        print("B")
    else:
        print("N")




