n = int(input())
l = list(map(int, input().split()))

max_l = max(l)
ml = []

for i in range(n):
    if l[i] == max_l:
        l[i] = 0
        ml.append(l[i])


if max_l < sum(l):
    print("Yes")
elif max_l >= sum(l):
    print("No")
