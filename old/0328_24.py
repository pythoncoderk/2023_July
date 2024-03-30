n, k = map(int, input().split())
l = [list(map(int, input().split())) for i in range(2)]

p = sum(l[0])
m = sum(l[1])

print(k + (p - m))