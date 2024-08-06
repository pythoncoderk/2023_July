l = [int(input()) for i in range(3)]

l2 = sorted(l, reverse=True)

d = {l2[k]: k + 1 for k in range(3)}

for _ in l:
    print(d[_])