n, k = map(int, input().split())
l = [int(input()) for _ in range(n)]
l2 = [input() for _ in range(k)]

for i in range(k):
    if l2[i] == "pop":
        if l:
            l.pop(0)
    elif l2[i] == "show":
        if l:
            for j in range(len(l)):
                print(l[j])
