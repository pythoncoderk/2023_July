n = int(input())
l = list(map(int, input().split()))

# print(n)
# print(l)

max_l = max(l)
min_l = min(l)

for i in range(len(l)):
    if l[i] == max_l:
        l.pop(i)
        break
for i in range(len(l)):
    if l[i] == min_l:
        l.pop(i)
        break

avg = sum(l) / len(l)
avg = str(avg)
avg_index = avg.index(".")
# print(avg_index)
print(avg[:avg_index+2])