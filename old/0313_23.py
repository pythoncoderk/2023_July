s = input()

count = -1

for i in range(len(s)):
    if s[i] == "a":
        count = i + 1
print(count)