n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

c = set(a + b)
print(*sorted(c))