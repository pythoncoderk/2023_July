s = list(input())

l = [str(i) for i in range(len(s)) if s[i] != "x"]
print(l)

l2 = [list(str(i).zfill(4)) for i in range(10000)]
# print(l2)

final_count = 0
for i in range(len(l2)):
    l_count = 0
    for j in range(4):
        if l2[i][j] in l:
            l_count += 1
    if l_count >= 4:
        final_count += 1
print(final_count)


