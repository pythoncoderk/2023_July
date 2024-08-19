a, b, c1 = map(int, input().split())

cx = a & b
sy = a ^ b

cy = sy & c1
s = sy ^ c1

c2 = cx ^ cy

print(c2, s)