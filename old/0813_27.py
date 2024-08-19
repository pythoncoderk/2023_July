l = [1, 5, 9, 7, 3, 2, 4, 8, 6, 10]
n = int(input())

for i in range(len(l)):
    if l[i] == n:
        print(i + 1)
        break