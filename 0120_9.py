n = input()
m = int(input())
l = [input() for i in range(m)]

count_l = 0
for i in range(m):
    if n not in l[i]:
        print(l[i])
        count_l += 1

if count_l == 0:
    print("none")