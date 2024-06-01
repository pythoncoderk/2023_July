n, a, b = map(int, input().split())
l1 = list(input())
la = list(input())
lb = list(input())

a_count = 0
for i in range(n):
    if len(la) >= 1:
        if l1[i] == la[0]:
            la.pop(0)
            a_count += 1

b_count = 0
for i in range(n):
    if len(lb) >= 1:
        if l1[i] == lb[0]:
            lb.pop(0)
            b_count += 1
print(a_count, b_count)

