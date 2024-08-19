l = [int(input()) for i in range(6)]

# print(l)

chk = True
for i in range(5):
    for j in range(5):
        if l[i] - l[j] > l[-1]:
            chk = False
            break

print("Yay!" if chk else ":(")