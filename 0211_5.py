l = [ "a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
s = input()
for i in range(len(s)):
    if s[i] not in l:
        print(s[i], end="")
