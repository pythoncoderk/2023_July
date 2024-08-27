n = int(input())
l = [input() for i in range(n)]
m = int(input())
l2 = [input() for i in range(m)]

for i in range(n):
    for j in range(m):
        print("YES" if l[i] in l2[j] else "NO")
