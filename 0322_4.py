l = [5, 9, 6, 1, 2, 7, 3, 8, 4]

for i in range(len(l)):
    for j in range(-1, len(l) * -1, -1):
        if l[j] < l[j-1]:
            l[j], l[j-1] = l[j-1], l[j]
print(l)
