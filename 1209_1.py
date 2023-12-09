n = int(input())
l = list(map(int, input().split()))
l2 = list(map(int, input().split()))
sc = sum(l)

if sc == 0:
    print(0)
elif sc >= 1:
    print("+")
else:
    print("-")