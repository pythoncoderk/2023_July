import copy

n = int(input())
l = [int(input()) for i in range(n)]
x, y = map(int, input().split())
l2 = copy.copy(l)
a = l.index(x)
b = l.index(y)
