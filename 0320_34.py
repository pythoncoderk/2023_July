n = int(input())

l = list(map(int, input().split()))
l.sort()
m = int(input())
l2 = [int(input()) for i in range(m)]

print(n)
print(m)
print(l)
print(l2)

for i in range(m):
    al = l[:]
    for j in range(n):
        a = len(al) // 2
        al1 = al[:a]
        al2 = al[a:]
        if l2[i] in al1:
            print("Yes")
            break
        else:
            al1 = al2


