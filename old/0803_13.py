n, q = map(int, input().split())
s = set(map(int, input().split()))

# print(n, q)
# print(s)
# print(type(s))

print("Yes" if q in s else "No")