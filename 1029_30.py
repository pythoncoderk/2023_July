x, y = map(int, input().split())
l = [int(input()) for i in range(x)]
if y in l:
    print("Yes")
else:
    print("No")