l = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
n = list(input())
x = 0
for i in n:
    if i in l:
        pass
    else:
        x += 1

if x == 0:
    print("YES")
else:
    print("NO")

