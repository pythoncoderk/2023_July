n = int(input())
m = int(input())
l = [input() for i in range(m)]
strs = input()
paswords = []
for i in range(n):
    if len(l) == 0:
        paswords.append(strs)
    else:
        ls = list(l[0].split())
        ls1 = int(ls[0])
        ls2 = ls[1]
        if ls1 == i + 1:
            paswords.append(ls2)
            l.pop(0)
        else:
            paswords.append(strs)
for i in paswords:
    print(i, end="")
