n = int(input())
l = [input() for i in range(n)]

for i in range(n):
    if l[i] == "strike":
        print("strike!")
    else:
        print(l[i])