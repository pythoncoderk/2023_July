import sys

k = int(input())
l = [int(input()) for i in range(9)]
l_counts = 0
ining = 1
for i in l:
    l_counts += i
    if l_counts > k:
        print(ining)
        sys.exit()
    else:
        ining += 1
print("Yes")