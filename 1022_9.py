n = int(input())
l = [i for i in range(1, n+1)]
l2 = []
for i in l:
    if n % i == 0:
        l2.append(i)
for i in l2:
    print(i)