l = [4, 0, 5, -1, 3, 10, 6, -8]
l2 = [l[i] for i in range(len(l)) if l[i] >= 5]
print(sum(l2))