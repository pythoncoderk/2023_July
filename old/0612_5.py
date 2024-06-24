l = list(map(int, input().split()))
l.sort()
x = l.pop(0)
total = 0
while l:
    y = l.pop(0)
    total += y - x
    x = y

print(total)