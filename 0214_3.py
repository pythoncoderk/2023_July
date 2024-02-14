a, b = map(str, input().split())
counta = 0
countb = 0
for i in range(1, 10):
    for j in range(10):
        ai = str(i)+str(j)
        ans = a + str(i) + b
        if int(ai) * int(j) == int(ans):
            counta = i
            countb = j
if counta == 0 and countb == 0:
    print("No")
else:
    print(counta, countb)
