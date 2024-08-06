
s = input()
x, y = map(str, input().split())

x = int(x)

print(s[:x - 1] + y + s[x:])