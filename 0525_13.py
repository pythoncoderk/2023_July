n, m = map(int, input().split())
l = list(map(int, input().split()))
l2 = list(map(int, input().split()))

# print(n, m)
# print(l)
# print(l2)

l.sort()
ab = l + l2
ab.sort()

a_l = []
for i in range(n-1):
    x = str(l[i])
    y = str(l[i+1])
    a_l.append(x + y)

total_l = []
for i in range(len(ab)-1):
    x = str(ab[i])
    y = str(ab[i+1])
    total_l.append(x + y)

chk = False
for i in range(len(l)-1):
    if a_l[i] in total_l:
        chk = True

if chk:
    print("Yes")
else:
    print("No")