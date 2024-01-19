s = input()
print(s)

l = [str(i).zfill(4) for i in range(10000)]
print(l)
judge = False
for i in range(len(l)):
    for j in range(10):
        if s[j] == "o":
            x = str(j)
            if x in 
