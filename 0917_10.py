l = list(map(str, input().split()))
x = input()

for i in range(len(l)):
    if l[i] == x:
        print(i)
        break