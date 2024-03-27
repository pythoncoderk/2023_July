n = int(input())
l = list(map(int, input().split()))

if n >= sum(l):
    print("OK")
else:
    print("NG")