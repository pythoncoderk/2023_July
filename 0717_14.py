n, q = map(int, input().split())
l = {int(input()) for i in range(n)}
l2 = [int(input()) for i in range(q)]

# print(n, q)
# print(l)
# print(l2)

for i in range(len(l2)):
    if l2[i] in l:
        print("YES")
    else:
        print("NO")