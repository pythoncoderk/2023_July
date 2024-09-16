l = list(map(str, input().split()))
l2 = []
for i in l:
    if i not in l2:
        print(i)
        l2.append(i)
    else:
        print("already_been")