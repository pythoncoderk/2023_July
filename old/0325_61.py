s = input()

for i in range(len(s)):
    if s[i] == "1":
        print("A", end="")
    elif s[i] == "2":
        print("B", end="")
    elif s[i] == "0":
        print("C", end="")