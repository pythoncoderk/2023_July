x = list(map(str, input()))


a = int(x[0]) * 100 + int(x[1]) * 10 + int(x[2])
b = int(x[2]) * 100 + int(x[0]) * 10 + int(x[1])
c = int(x[1]) * 100 + int(x[2]) * 10 + int(x[0])

print(a + b + c)
