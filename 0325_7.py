l = list(map(int, input().split()))
n = int(input())

l2 = (sum(l) / len(l))
if l2 >= n:
    print("pass")
else:
    print("failure")