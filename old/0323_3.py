n, t, s = map(str, input().split())
n = int(n)

# print(n, t, s)

if t == s:
    print(0)
    exit()

count = 0
while True:
    x = s[0]
    y = s[1:]
    s = y + x
    count += 1
    if t == s:
        break
print(count)