n = list(input())
l = [int(n[i]) for i in range(len(n))]
l.reverse()

l2 = [l[i] * (2 ** i) for i in range(len(n))]
print(sum(l2))