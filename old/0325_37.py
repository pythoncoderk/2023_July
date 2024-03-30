n = list(map(str, input().split()))

x = n[0] + n[1]

if x.count(x[0]) == len(x):
    print("Yes")
else:
    print("No")