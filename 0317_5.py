n = list(input())
n2 = n[::]
n3 = n[::]

two1 = n2[1]
two2 = n2[-1]
two3 = n2[0]


three1 = n3[:2]
three2 = n3[-1]

x = ""
for i in range(3):
    x += n[i]
x = int(x)

# print(x)

y = ""
for i in range(1):
    y += two1
    y += two2
    y += two3
y = int(y)

# print(y)

z = str(three2)
for i in range(2):
    z += three1[i]
z = int(z)
# print(z)

print(x + y + z)


