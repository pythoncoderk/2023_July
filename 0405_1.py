n = input()


while str(n) != str(n)[::-1]:
    n = str(n)
    m = int(n[::-1])
    n = int(n) + m
print(n)
