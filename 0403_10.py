l = [1, 1]
for i in range(21):
    l.append(l[i] + l[i+1])

n = int(input())
print(l[n-1])