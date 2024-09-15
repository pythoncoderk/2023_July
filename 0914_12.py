l = list(input())

l_num = []
for i in range(len(l)):
    if l[i] != "x":
        l_num.append(str(i))

must_l = []
for i in range(len(l)):
    if l[i] == "o":
        must_l.append(str(i))

print(l_num)
ans = 0
count = 0
while count < 10000:
    count_num = str(count).zfill(4)
    l_count_num = list(str(count_num))
    if l_count_num[0] in l_num:
        if l_count_num[1] in l_num:
            if l_count_num[2] in l_num:
                if l_count_num[3] in l_num:
                    for_count = 0
                    for i in must_l:
                        if i in l_count_num:
                            for_count += 1
                        else:
                            break
    if for_count == len(l_count_num) - 1:
        ans += 1
    count += 1

print(ans)
