n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

# print(n)
# print(l)

l2 = [i + 1 for i in range(n) if l[i][0] == "n" or l[i][1] == "n"]
# print(l2)

print(len(l2))
for i in l2:
    print(i)

