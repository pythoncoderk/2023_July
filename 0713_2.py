l = list(map(int, input().split()))
c = input()

if c == "Red":
    l.pop(0)
elif c == "Green":
    l.pop(1)
else:
    l.pop(2)

print(min(l))