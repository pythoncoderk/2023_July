s = input()
count_l = []
for i in range(len(s)):
    count_l.append(s.count(s[i]))
max_l = max(count_l)
abc = []
for i in range(len(s)):
    if s.count(s[i]) == max_l:
        abc.append(s[i])
# print(abc)
abc_s = set(abc)
abc_l = list(abc_s)
abc_f = sorted(abc_l)
print(abc_f[0])