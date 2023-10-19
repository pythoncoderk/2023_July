n = list(input())


while len(n) != 1:
    x = int(n.pop(0))
    y = n.pop(0)
    z = int(n.pop(0))
    if y == "+":
        n.insert(0, (x + z))
    else:
        n.insert(0, (x - z))
print(n[0])
