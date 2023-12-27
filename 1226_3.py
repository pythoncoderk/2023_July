n, m = map(int, input().split())
if n % 2 == 0 and m % 2 == 0:
    print("NO")
elif n % 2 != 0 and m % 2 != 0:
    print("NO")
else:
    print("YES")