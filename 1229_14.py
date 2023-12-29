s = list(input())
l = [s.count(s[i]) for i in range(len(s)) if s.count(s[i]) >= 20]
if l == []:
    print("OK")
else:
    print("NG")