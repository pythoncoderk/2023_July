n, k = map(int, input().split())
s = input()

text = ""
for i in range(len(s)):
    if k - 1 == i:
        text += s[i].lower()
    else:
        text += s[i]

print(text)