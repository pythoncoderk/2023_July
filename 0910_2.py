def linsearch(a, p):
    for i in range(0, len(a), 1):
        if a[i] == p:
            print("見つかりました！添字:", i)
            break

a = [61,15,82,77,21,32,53]
p = 82

print(linsearch(a, p))