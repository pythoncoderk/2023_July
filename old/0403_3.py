n, m = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

l2 = []
key1 = ["en", "jp", "math"]
for i in range(n):
    x = dict(zip(key1, l[i]))
    l2.append(x)

d_count = 1
for i in l2:
    i["No"] = d_count
    d_count += 1

print(l2)

for i in range(n):
    rank = 1
    count = 0
    last_score = None
    for j in range(len(key1)):
        x = sorted(l2, key=lambda k: k[key1[j]])
        if last_score !=
