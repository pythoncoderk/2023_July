a, b = map(int, input().split())

l = [i for i in range(a, b+1) if i % 2 == 0 or i % 3 == 0]

print(len(l))