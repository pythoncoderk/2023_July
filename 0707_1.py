n, k = map(int, input().split())
l = [input() for i in range(n)]
l2 = [input() for i in range(k)]

for i in range(k):
    if l2[i] == "pop":
        l.pop(0)
    elif l2[i] == "show":
        for j in range(len(l)):
            print(l[j])