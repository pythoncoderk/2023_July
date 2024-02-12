import sys

s = list(input())
t = list(input())

if len(s) != len(t):
    print("NO")
    sys.exit()
elif s == t:
    print("NO")
    sys.exit()

s.sort()
t.sort()

if s == t:
    print("YES")
else:
    print("NO")






