n = int(input())
m = int(input())

print(0 if n % m == 0 else m - n % m)