n = int(input())
x = 65
num = [0, 0, 0]
for i in range(n):
    x += 1
    if x >= 91:
        if num[0] >= 90:
            if num[1] >= 90:
                num[2] += 1
                x = 65
            else:
                num[1] += 1
                x = 65
        else:
            num[0] += 1
            x = 65
final = ""
for i in range(3):
    if num[i] != 0:
        final += chr(num[i] + 65)