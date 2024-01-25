l = list(map(str, input().split()))
l2 = l[::]
final_l = []
x = 0
y = 0
while x < 4:
    a = l2.pop(x)
    b = l2.pop(y)
    c = l2.pop(0)
    d = l2.pop(0)
    final_l.append(int(a + b) + int(c + d))
    final_l.append(int(a + b) + int(d + c))
    final_l.append(int(b + a) + int(d + c))
    final_l.append(int(b + a) + int(c + d))
    x += 1
    l2 = l[::]

print(max(final_l))