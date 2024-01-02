n = int(input())
l = [int(input()) for i in range(n)]
l2 = []
for i in range(n):
    for j in range(1, n):
        if l[i] + l[j] == 777:
            l2.append(l[i])
            l2.append(l[j])
if len(l2) >= 3:
    print("multiple answers")
elif l2 == []:
    print("no answer")
else:
    print(f"{min(l2)} {max(l2)}")