l = [int(input()) for i in range(3)]
n = int(input())
print(n)
print(l)
total = []
for i in range(3):
    chk = []
    for j in range(i, len(l)-1):
        chk