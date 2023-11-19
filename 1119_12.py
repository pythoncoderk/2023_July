l = list(map(int, input().split()))
n = int(input())
l2 = sum(l) // len(l)
if n <= l2:
    print("pass")
else:
    print("failure")