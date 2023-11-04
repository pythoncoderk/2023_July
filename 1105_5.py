l = [input() for i in range(3)]
x = len(l[0])
for i in range(2):
    if x < len(l[i+1]):
        x = len(l[i+1])
print(x)