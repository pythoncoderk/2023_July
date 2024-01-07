a, b = map(int, input().split())
s = input()

x_1 = s[:a-1]
x = s[a-1:b].upper()
x_2 = s[b:]

print(x_1 + x + x_2)
