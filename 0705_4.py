n, l, r = map(int, input().split())

l2 = [i for i in range(1, n + 1)]

# print(l2)

x = l2[:l - 1]
y = l2[l - 1:r]
y.sort(reverse=True)
z = l2[r:]

# print(x)
# print(y)
# print(z)

l3 = x + y + z

print(*l3)