n = int(input())
l = [0, 1]
for i in range(n-2):
    l.append(l[-2] + l[-1])
for i in l:
    print(i)