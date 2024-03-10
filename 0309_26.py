n = int(input())
a_l = list(map(int, input().split()))
m = int(input())
b_l = list(map(int, input().split()))
ll = int(input())
c_l = list(map(int, input().split()))
q = int(input())
x_l = list(map(int, input().split()))

l = []

for i in range(n):
    xx = 0
    for j in range(m):
        for k in range(ll):
            l.append(a_l[i] + b_l[j] + c_l[k])

for i in range(q):
    if x_l[i] in l:
        print("Yes")
    else:
        print("No")