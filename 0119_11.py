s = input()

l = [str(i).zfill(4) for i in range(10000)]
print(l)

for i in range(10000):
    for j in range(10):
        if s[j] == "o":
            if str(i) not in l[i]:
                break
            