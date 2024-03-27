n, t, s = map(str, input().split())

# print(n, t, s)
count = 0
if t == s:
    print(0)
    exit()

for i in range(int(n)):
    x = s[0]
    y = s[1:]
    s = y + x
    if t == s:
        count += 1
        break
    else:
        count += 1
print(count)
