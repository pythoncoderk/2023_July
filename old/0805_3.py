n = int(input())
s1 = set(input().split())
s2 = set(input().split())

x = list(s1 | s2)
xx = sorted(x)
print(*xx)