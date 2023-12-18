n = int(input())
l = []
while n != 0:
    x = n % 2
    n //= 2
    l.append(str(x))
l.reverse()
print("".join(l))