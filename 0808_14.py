s = input()
ss = set()

for i in s:
    if i not in ss:
        ss.add(i)
        print(i, end="")