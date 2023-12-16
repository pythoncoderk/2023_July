l = [i for i in range(10) if i % 2 == 0]
print(l)

d = {i: "even" if i % 2 == 0 else "odd" for i in range(10)}
print(d)

l2 = [i + j for i in (10, 100, 1000) for j in (1, 2, 3)]
print(l2)

