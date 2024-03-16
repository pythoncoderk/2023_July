s = input()

for i in range(len(s)+1):
    if str(i) not in s:
        print(i)