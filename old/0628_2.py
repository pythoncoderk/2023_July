n = input()
m = int(input())

x = int(n[:len(n)-m])

y = int(n[m*-1])

if y >= 5:
    x += 1

l = "0" * m

print(str(x) + l)

