n = int(input())
l = list(map(int, input().split()))
l2 = list(map(int, input().split()))

l3 = [l[i] * l2[i] for i in range(n)]
if sum(l3) == 0:
    print("Yes")
else:
    print("No")