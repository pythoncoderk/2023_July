n = int(input())

s = ""
while n != 0:
    x = n % 2
    s += str(x)
    n //= 2

f = s[::-1]
print(f.zfill(10))


