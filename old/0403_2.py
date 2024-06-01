n, m = map(int, input().split())

l = [list(map(int, input().split())) for i in range(n)]

print(n, m)
print(l)

key1 = ["eng", "lang", "math"]
l2 = []
for i in range(n):
    x = dict(zip(key1, l[i]))
    l2.append(x)
q = 1
for i in l2:
    i["No"] = q
    q += 1

print(l2)

for xxx in range(n):
    x = sorted(l2, key=lambda e: e[key1[xxx]])
    rank = 1
    count = 0
    last_score = None
    for i in x:
        if last_score != i[key1[xxx]]:
            rank += count
            count = 0
            last_score =i[key1[xxx]]
        i["rank"] = rank
        count += 1
    print(l2)


