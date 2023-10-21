n = int(input())
for i in range(9):
    if i == 8:
        print(n * (i+1))
    else:
        print(n * (i+1), end=" ")