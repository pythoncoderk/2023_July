n, q = map(int, input().split())
l = [list(map(str, input().split())) for i in range(q)]
l2 = [i+1 for i in range(n)]

for i in range(q):
    if l[i][0] == "reverse":
        l2.reverse()
    elif l[i][0] == "swap":
        x = l2[int(l[i][1])-1]
        y = l2[int(l[i][2])-1]
        l2[(int(l[i][1]) - 1)] = y
        l2[(int(l[i][2]) - 1)] = x
    elif l[i][0] == "resize":
        l2 = l2[:(int(l[i][1]))]
for i in l2:
    print(i)
