l = [int(input()) for i in range(7)]
l = [l[i] for i in range(7) if l[i] <= 30]
print(len(l))