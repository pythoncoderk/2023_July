n, l, r = map(int, input().split())

# print(n, l, r)

li = [i for i in range(1, n + 1)]

# print(li)

x = li[:l-1]
y = li[r:]
z = li[l-1:r][::-1]

# print(x)
# print(y)
# print(z)

if x == [] and y == []:
    print(*z)
elif not x:
    final = z + y
    print(*final)
else:
    final = x + z + y
    print(*final)