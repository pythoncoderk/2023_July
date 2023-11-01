l = list(map(int, input().split()))
avg = int(input())
if sum(l) / len(l) >= avg:
    print("pass")
else:
    print("failure")