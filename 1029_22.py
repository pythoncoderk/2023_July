n = int(input())
l = list(map(int, input().split()))
a = sum(l)/len(l)
for i in l:
    if i >= a:
        print(i)