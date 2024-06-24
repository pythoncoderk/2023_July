s = input()

y = s[:s.index("/")]
# print(y)

m = s[s.index("/") + 1:s.rfind("/")]
# print(m)

d = s[s.rfind("/") + 1:]
# print(d)

answer = int(y + m + d)

print("Heisei" if answer <= 20190430 else "TBD")