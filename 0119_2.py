s = input()
count = 0
for num in range(10000):
    ok = True
    num = str(num)
    num=num.zfill(4)

    for i in range(10):
        if s[i] == "o":
            if str(i) not in num:
                ok = False
        if s[i] == "x":
            if str(i) in num:
                ok = False
    if ok == True:
        count += 1
print(count)