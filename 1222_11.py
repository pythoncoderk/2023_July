a, b = map(int, input().split())
l = [i for i in range(a, a+(b*10), b)]
print(*l)