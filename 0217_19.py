n = int(input())
x = list("0" * n)
y = list("1" * (n+1))

# print(x)
# print(y)

for i in range(len(y)+len(x)):
    if i % 2 == 0:
        print(y.pop(0), end="")
    else:
        print(x.pop(0), end="")