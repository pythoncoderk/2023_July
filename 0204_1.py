l = list(map(str, input().split()))
# print(l)

count_l = []
for i in l:
    if i not in count_l:
        count_l.append(i)
# print(count_l)

for i in range(len(count_l)):
    print(f"{count_l[i]} {l.count(count_l[i])}")