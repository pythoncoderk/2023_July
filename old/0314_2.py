n = int(input())
l = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "0"]

x = n // 16
y = n % 16

print(f"{l[x-1]}{l[y-1]}")


