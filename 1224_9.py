l = list(map(int, input().split()))
n = int(input())

avg = sum(l) / len(l)
if avg >= n:
    print("OK")
else:
    print("NG")