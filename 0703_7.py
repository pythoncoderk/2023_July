a, b, c, d = map(int, input().split())

# print(a, b, c, d)

print(int(not((int(not a)&int(not b))|int(not c)))^d)