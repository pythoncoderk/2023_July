n, k = map(int, input().split())
l = [[int(input()) for j in range(n)] for i in range(3)]

# print(n, k)
# print(l)

final = []
for i in range(3):
    l3 = []
    for j in range(n-k+1):
        l2 = []
        for q in range(j, j+k):
            l2.append(l[i][q])
        l3.append(sum(l2)/len(l2))
    final.append(min(l3))

final_min = min(final)
for i in range(len(final)):
    if final[i] == final_min:
        print(i+1)
        break

