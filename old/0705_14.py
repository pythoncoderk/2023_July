n = int(input())

if "3" in str(n):
    print("YES")
    exit()

print("YES" if n % 3 == 0 else "NO")