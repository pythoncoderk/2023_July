def linsearch(a, p):
    for i in range(0, len(a), 1):
        if a[i] == p:
            print("見つかりました！" + str(i + 1) + "番目！",)
            break

a = [61, 15, 82, 77, 21, 32, 53]
p = 82

linsearch(a, p)