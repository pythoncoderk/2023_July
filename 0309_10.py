n, m, p = map(int, input().split())

l = [i for i in range(m, n+1, p)]
print(len(l))