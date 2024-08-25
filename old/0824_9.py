n = int(input())
l = list(map(int, input().split()))

count = 0
while True:
    x = len(l)
    y = l.count(0)
    if x - 1 != y and x != y:
        l.sort(reverse=True)
        l[0] -= 1
        l[1] -= 1
        count += 1
    else:
        break

print(count)


