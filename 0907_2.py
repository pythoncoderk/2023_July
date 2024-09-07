l, r = map(int, input().split())

if l == 1 and r == 0:
    print("Yes")
elif l == 0 and r == 1:
    print("No")
elif (l == 1 and r == 1) or (l == 0 and r == 0):
    print("Invalid")