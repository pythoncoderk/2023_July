s = input()

count = 0
for i in range(len(s)):
    if s[i] == "o":
        count += 100

print(700 + count)