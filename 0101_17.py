n = int(input())
l = [input() for i in range(n)]
l2 = []

for i in l:
    if i in l2:
        print("NO")
    else:
        l2.append(i)
        print("YES")