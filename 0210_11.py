n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
# print(n)
# print(l)
l2 = l[::]
x = 0
ok = 0
while True:
    if l2:
        y1 = l2[0]
        del l2[0]
        for i in range(len(l2)):
            if l2[i][0] == y1[0]:
                if y1[1] == "R":
                    if l2[i][1] == "L":
                        ok += 1
                        del l2[i]
                        break
                else:
                    if l2[i][1] == "R":
                        ok += 1
                        del l2[i]
                        break
    else:
        break
print(ok)

