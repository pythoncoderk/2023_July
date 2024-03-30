l = list(map(int, input().split()))
l2 = list(map(int, input().split()))

if sum(l) < sum(l2):
    print(sum(l))
else:
    print(sum(l2))