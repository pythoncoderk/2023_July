l = [2, 5, 1, 4, 6, 3]

for i in range(1, len(l)):
    tmp = l[i]
    for j in range(i - 1, -1, -1):
        if tmp < l[j]:
            l[j + 1] = l[j]
        else:
            l[j + 1] = tmp
            break

    else:
        l[0] = tmp

print(l)




