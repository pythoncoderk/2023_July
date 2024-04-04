x, y = map(int, input().split())
l = [list(map(int, input().split())) for i in range(x)]

# print(x, y)
# print(l)

test = ["en", "jp", "math"]

l2 = []
for i in range(x):
    d = dict(zip(test, l[i]))
    d["No"] = i+1
    l2.append(d)
# print(l2)

for i in range(3):
    rank = 0
    count = 0
    last_score = None
    d2 = sorted(l2, key=lambda k: k[test[i]])
    for j in range(x):
        if d2[j][test[i]] != last_score:
            rank += 1 + count
            last_score = d2[j][test[i]]
            d2[j][f"{test[i]}_rank"] = rank
            count = 0
        else:
            d2[j][f"{test[i]}_rank"] = rank
            count += 1
d2 = sorted(d2, key=lambda k: k["No"])
# print(d2)

for i in range(x):
    count = 0
    for j in range(3):
        if d2[i][f"{test[j]}_rank"] <= y:
            count += 1
    print(count)