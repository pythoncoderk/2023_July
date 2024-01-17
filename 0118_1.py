s = list(input())
print(s)

l = [(str(i).zfill(4)) for i in range(1000)]
print(l)

yes_l = [str(i) for i in range(len(s)) if s[i] == "o"]
no_l = [str(i) for i in range(len(s)) if s[i] == "x"]
print(yes_l)
print(no_l)
l_count = 0
for i in l:
    for j in range(len(no_l)):
        if no_l[j] in i:
            break
        else:
            for k in range(len(yes_l)):
                if yes_l[k] not in i:
                    break
        l_count += 1
print(l_count)

