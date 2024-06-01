x, y = map(int, input().split())
l = [list(map(int, input().split())) for i in range(x)]

print(x, y)
print(l)

test = ["en", "lang", "math"]

l2 = []
for i in range(x):
    l2.append(dict(zip(test, l[i])))
print(l2)

en_rank = list(sorted(l2, key=lambda k: k["en"]))
print(en_rank)

rank = 1
count = 0
last_score = None

for i in range(x):
    for j in l2[i]:
        if last_score != j[test[i]]:
            rank += count
            count = 0
            last_score = j[test[i]]
        j[test[i]] = rank
        count += 1
