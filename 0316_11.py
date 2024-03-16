s = input()

if s[0] == "<" and s[-1] == ">":
    if len(s[1:-1]) == s.count("="):
        print("Yes")
    else:
        print("No")
else:
    print("No")