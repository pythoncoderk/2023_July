n = int(input())
s = input()

# print(n)
# print(s)

for i in range(len(s)):
    if (i+1) % 2 == 0:
        if ord(s[i])+n > 90:
            x = ord(s[i])+n - 90 + 64
            print(chr(x), end="")
        else:
            x = ord(s[i]) + n
            print(chr(x), end="")
    else:
        if ord(s[i])-n < 65:
            x = 91 - (65 - (ord(s[i])-n))
            print(chr(x), end="")
        else:
            x = (ord(s[i]) - n)
            print(chr(x), end="")