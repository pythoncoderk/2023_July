n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

# print(n)
# print(l)
count = 0
f_l = []
for i in range(n):
    if l[i][0] != "y" or l[i][1] != "y":
        count += 1
        f_l.append(i+1)
print(count)
for i in f_l:
    print(i)
