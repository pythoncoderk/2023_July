l = list(map(str, input().split()))
while l:
    x = l[0]
    print(l[0], l.count(l[0]))
    new_l = []
    for i in l:
        if i != x:
            new_l.append(i)

    l = new_l
