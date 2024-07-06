n = int(input())
l = [int(input()) for i in range(n)]

# print(n)
# print(l)

l.pop(0)
for i in l:
    print(i)