n = list(map(int, input()))
# print(n)

chk = True
for i in range(len(n)-1):
    if n[i] <= n[i+1]:
        chk = False
        break
if chk:
    print("Yes")
else:
    print("No")