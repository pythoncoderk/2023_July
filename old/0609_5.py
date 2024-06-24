s = input()

chk = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        chk += 1

print("Bad" if chk >= 1 else "Good")