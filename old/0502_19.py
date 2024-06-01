s = input()
t = input()

# print(s)
# print(t)

chk = True
if s == t or len(s) != len(t):
    chk = False

s = list(s)
t = list(t)

s.sort()
t.sort()

if s != t:
    chk = False

if chk:
    print("YES")
else:
    print("NO")




