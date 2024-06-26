l = list(map(str, input().split()))
s = input()

for i in range(len(l)):
    if l[i] == s:
        print(i)
        break