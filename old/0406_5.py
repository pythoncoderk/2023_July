s = input()
t = input()

if s != t:
    if sorted(s) == sorted(t):
        print("YES")
    else:
        print("NO")
else:
    print("NO")