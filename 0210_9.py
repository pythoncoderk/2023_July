n, m = map(int, input().split())
l = [int(input()) for i in range(n)]

# print(n, m)
# print(l)
counts_l = []
count = 0
check = False
for i in range(n):
    if len(counts_l) == m:
        check = True
        break
    else:
        if l[i] not in counts_l:
            counts_l.append(l[i])
            count += 1
        else:
            count += 1
if check == False:
    print("unlucky")
else:
    print(count)

