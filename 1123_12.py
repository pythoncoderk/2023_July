m, n = map(int, input().split())
l_m = [i+1 for i in range(m-1)]
l_n = [i+1 for i in range(n-1)]
counts = 0
for i in range(len(l_m)):
    for j in range(len(l_n)):
        x = l_m[i] ** 2
        y = l_n[j] ** 2
        if ((x % 3 == 0 and y % 4 == 0 and (x + y) % 5 == 0)
                or (x % 4 == 0 and y % 3 == 0 and (x + y) % 5 == 0)):
            counts += 1
print(counts//3)