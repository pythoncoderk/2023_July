n = int(input())

l = [input() for i in range(n)]

# print(l)
x = l.pop(0)
while l:
    if l[0] == "sweet" and x == "sweet":
        l.pop(0)
        break
    else:
        x = l.pop(0)

print("Yes" if len(l) == 0 else "No")