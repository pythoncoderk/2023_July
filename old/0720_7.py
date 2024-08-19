n, t, p = map(int, input().split())
l = list(map(int, input().split()))

# print(n, t, p)
# print(l)

count = 0

while True:
    counta = 0
    for i in range(n):
        if l[i] >= t:
            counta += 1
    if counta >= p:
        print(count)
        exit()
    else:
        count += 1
        for i in range(n):
            l[i] += 1



