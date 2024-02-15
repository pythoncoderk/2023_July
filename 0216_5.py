n = int(input())
l = [int(input()) for i in range(n)]
len_l = l[::]

# print(n)
# print(l)
days_total = []
days = []
x = l.pop(0)
len_days = 0
while len_days < len(len_l):
    if not l:
        days.append(x)
        days_total.append(days)
        break
    else:
        if x + 1 == l[0]:
            days.append(x)
            x = l.pop(0)
            len_days += 1
        else:
            days.append(x)
            days_total.append(days)
            x = l.pop(0)
            days = []
            len_days += 1
# print(days_total)

l2 = []
for i in range(len(days_total)):
    l2.append(len(days_total[i]))
# print(l2)
max_l = max(l2)

for i in range(len(l2)):
    if l2[i] == max_l:
        print(days_total[i][0], days_total[i][-1])
        break

