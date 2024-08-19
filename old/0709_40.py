s = input()

answer = False
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        answer = True

print("Bad" if answer else "Good")