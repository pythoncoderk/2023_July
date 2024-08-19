n = int(input())

if n == 0:
    print("No")
    exit()

print("Yes" if n % 100 == 0 else "No")