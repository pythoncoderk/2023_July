w, b = map(int, input().split())

if (w % 3 == 0 or w % 4 == 0) and b % 2 == 0 and w != 0 and b != 0:
    print("Yes")
else:
    print("No")