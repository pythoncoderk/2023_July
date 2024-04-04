x, y = map(int, input().split())
l = [list(map(int, input().split())) for i in range(x)]

# print(x, y)
# print(l)

cate = ("en", "lang", "math")
# print(cate)

l2 = []
for i in range(x):
    d_x = dict(zip(cate, l[i]))
    l2.append(d_x)

for i in range(x):
    l2[i]["No"] = i+1

# print(l2)


for i in range(3):
    rank = 0
    count = 0
    last_score = None
    xxx = sorted(l2, key=lambda k: k[cate[i]])
    for j in range(x):
        if xxx[j][cate[i]] == last_score:
            xxx[j][f"{cate[i]}_rank"] = rank
            count += 1
        else:
            rank += 1 + count
            last_score = xxx[j][cate[i]]
            xxx[j][f"{cate[i]}_rank"] = rank
            count = 0
    # print(xxx)
xxx = sorted(xxx, key=lambda k: k["No"])
# print(xxx)
count = 0
for i in range(x):
    for j in range(3):
        if xxx[i][f"{cate[j]}_rank"] <= y:
            count += 1
    print(count)
    count = 0