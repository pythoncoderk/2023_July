n, t, s = map(str, input().split())

# print(n, t, s)

count = 0
while t != s:
    s = s[1:] + s[0]
    count += 1
print(count)