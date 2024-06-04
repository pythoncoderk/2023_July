a, b = map(str, input().split())

# print(a, b)

a = list(a)
b = list(b)

a = [int(a[i]) for i in range(len(a))]
b = [int(b[i]) for i in range(len(b))]

print(sum(a) if sum(a) > sum(b) else sum(b))