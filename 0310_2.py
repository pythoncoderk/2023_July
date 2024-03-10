n = int(input())
s = input()
t = input()

chk = True
for i in range(n):
    if (s[i] == "1" and t[i] == "l") or (s[i] == "l" and t[i] == "1"):
        chk = True
    elif (s[i] == "0" and t[i] == "o") or (s[i] == "o" and t[i] == "0"):
        chk = True
    elif s[i] != t[i]:
        chk = False
        break

if chk:
    print("Yes")
else:
    print("No")