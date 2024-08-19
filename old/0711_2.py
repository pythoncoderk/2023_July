n = int(input())

l = [list(input()) for i in range(n)]

# print(n)
# print(l)

x = l.pop(0)
for i in range(n - 1):
    l2 = []
    for j in range(4):
        l2.append(int(l[i][j]) ^ int(x[j]))
    x = l2
answer = ""
for i in range(len(x)):
    answer += str(x[i])

print(answer)