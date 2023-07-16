dic = {1: 2, 3: 4}

x = {k + v for k, v in dic.items()}
print(x)

y = {i: k**2 for i, k in dic.items()}
print(y)

z = {i**2: k**2 for i, k in dic.items()}
print(z)