n = int(input())

l = [list(map(str, input().split())) for i in range(n)]
m = input()
# print(n)
# print(l)

for i in range(n):
    if l[i][1] == m:
        print(l[i][0])



a, b = 2, 3

if a > b:
    print("a")
else:
    print("b")