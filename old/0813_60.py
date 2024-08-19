n = int(input())
l = list(map(int, input().split()))
av = sum(l) / n

for i in l:
    if i >= av:
        print(i)