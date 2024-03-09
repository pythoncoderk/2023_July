s = input()

chk = True
for i in range(len(s)):
    if i % 2 != 0:
        if s[i] != "0":
            chk = False
if chk:
    print("Yes")
else:
    print("No")
