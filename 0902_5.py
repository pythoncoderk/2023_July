l = input().split()
while l:
    print(l[0], l.count(l[0]))

    new_l = []
    for i in l:
        if i != l[0]:
            new_l.append(i)
        else:
            pass
    l = new_l