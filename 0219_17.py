n = int(input())
l = [input() for i in range(n)]

# print(n)
# print(l)
ng = 0
for i in range(n-1):
    if l[i][-1] != l[i+1][0]:
        ng1 = l[i][-1]
        ng2 = l[i+1][0]
        ng += 1
        break
if ng == 1:
    print(ng1, ng2)
else:
    print("Yes")