n = int(input())
l = list(map(int, input().split()))
l2 = l[::]
l2 = set(l2)
l2 = list(l2)
ranks = sorted(l2, reverse=True)
# print(n)
# print(l)
# print(ranks)

ranks_counts = []
for i in range(len(ranks)):
    ranks_counts.append(l.count(ranks[i]))
ranks_counts.insert(0, 0)
ranks_counts.pop()
# print(ranks_counts)

for i in range(n):
    for j in range(len(ranks)):
        if l[i] == ranks[j]:
            if ranks_counts[j] <= 1:
                if ranks.index(l[i]) == 0:
                    print("G")
                elif ranks.index(l[i]) == 1:
                    print("S")
                elif ranks.index(l[i]) == 2:
                    print("B")
                else:
                    print("N")
            else:
                print("N")
