n = int(input())
l = list(map(int, input().split()))

if l.count(l[0]) == len(l):
    print("Yes")
else:
    print("No")