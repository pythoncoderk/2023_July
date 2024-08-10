s = list(input())
n = int(input())

ss = set()
for i in s:
    for j in s:
        ss.add(i + j)

ss_final = sorted(ss)
print(ss_final[n - 1])