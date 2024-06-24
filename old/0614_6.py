n = int(input())
a = int(input())

if n < 500:
    print("Yes" if n <= a else "No")
else:
    x = n % 500
    print("Yes" if x <= a else "No")