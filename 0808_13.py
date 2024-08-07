l = list(input())

l2 = []
for i in l:
    if i not in l2:
        print(i, end="")
        l2.append(i)

