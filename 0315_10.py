s = list(input())
s2 = s[::]
s3 = s[::]
while len(s3) < 6:
    if not s2:
        s2 = s[::]
        s3.append(s2.pop(0))
    else:
        s3.append(s2.pop(0))

for i in s3:
    print(i, end="")