n = list(input())
if "." in n:
    print("少数")
else:
    while n[0] == '0':
        n.pop(0)
for i in n:
    print(i, end="")