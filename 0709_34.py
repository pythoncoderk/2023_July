n = int(input())
s = input()
l = [input() for i in range(n)]

# print(n)
# print(s)
# print(l)

chk = False
for i in range(n):
    if s in l[i]:
        print(l[i])
        chk = True

if not chk:
    print("None")