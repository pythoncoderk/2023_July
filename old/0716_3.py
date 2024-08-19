n = int(input())
s = input()


def change_odd(x, y):
    x = ord(x) - y
    if x <= 64:
        x = 91 - (65 - x)
    return chr(x)

def change_even(x, y):
    x = ord(x) + y
    if x >= 91:
        x = x - 91 + 65
    return chr(x)

answer = ""
for i in range(len(s)):
    if i % 2 == 0:
        answer += change_odd(s[i], n)
    else:
        answer += change_even(s[i], n)

print(answer)