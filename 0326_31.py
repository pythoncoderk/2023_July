s = input()

l = [s.count(s[i]) for i in range(len(s))]
# print(l)

if max(l) >= 2:
    print("NG")
else:
    print("OK")