n = int(input())
l = [int(input()) for i in range(n)]
l_min = min(l)
l_max = max(l)
print(l.index(l_min)+1)
if l_min == l_max:
    print("No")
else:
    print(l.index(l_max)+1)