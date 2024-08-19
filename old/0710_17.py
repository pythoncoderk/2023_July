l = list(map(str, input().split()))
l[0] = int(l[0])

# print(l)

count = 0
while True:
    if l[1] == l[2]:
        break
    else:
        x = l[2][1:]
        y = l[2][0]
        l[2] = x + y
        count += 1

print(count)