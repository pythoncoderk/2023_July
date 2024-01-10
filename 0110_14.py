n, q = map(int, input().split())
l = [int(input()) for i in range(n)]
l2 = [int(input()) for i in range(q)]

for i in range(q):
    for j in range(n):
        yes_or_no = 0
        if l2[i] == l[j]:
            yes_or_no += 1
            break
    if yes_or_no >= 1:
        print("YES")
    else:
        print("NO")