n = int(input())

l = []
while n != 0:
    y = n % 2
    n //= 2
    l.append(y)

l.reverse()
final = ""
for i in range(len(l)):
    final += str(l[i])

print(final.zfill(10))