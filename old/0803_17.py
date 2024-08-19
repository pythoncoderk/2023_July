n = int(input())
l = list(map(int, input().split()))
l2 = l[::]
l2.sort(reverse=True)
x = l2[1]

print(l.index(x) + 1)