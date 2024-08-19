n = int(input())
l = [int(input()) for i in range(n)]
b = int(input())

l.append(b)

for i in l:
    print(i)