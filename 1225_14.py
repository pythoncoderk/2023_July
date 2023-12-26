l = list(map(int, input().split()))
l2 = [l[i] for i in range(len(l)) if l[i] <= 2]
print(len(l2))