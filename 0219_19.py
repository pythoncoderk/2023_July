import sys

n, m = map(int, input().split())
l = list(map(int, input().split()))

# print(n, m)
# print(l)

if len(l) == l.count(0):
    print("NG")
    sys.exit()
elif len(l) == l.count(1):
    print("OK")
    sys.exit()

count = 1
for i in range(n-1):
    if l[i] == l[i+1] and l[i] == 0:
        count += 1
        if count >= m:
            print("NG")
            sys.exit()
    else:
        count = 1
print("OK")