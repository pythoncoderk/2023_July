n = int(input())
l = [int(input()) for i in range(n)]
l2 = [l[i] for i in range(n) if l[i] >= 5]
print(sum(l2))