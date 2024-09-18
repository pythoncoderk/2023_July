[p, q, r] = [int(i) for i in input().split()]
AB = {}
BC = {}

for _ in range(p):
    [x, j] = [int(n) for n in input().split()]
    AB[x] = j

for _ in range(q):
    [j2, k] = [int(n) for n in input().split()]
    BC[j2] = k

AC = {}

for i in range(1, p + 1):
    AC[i] = BC[AB[i]]

for i, k in AC.items():
    print(i, k)