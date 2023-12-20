n = int(input())
l = list(map(int, input().split()))
k = int(input())
l2 = [l[i] for i in range(n) if k <= l[i]]
print(min(l2))