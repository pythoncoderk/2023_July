n = int(input())
l = [input() for i in range(n)]

st = 0
for i in range(n):
    if l[i] == "strike":
        print("strike!")
        st += 1
        print(st)
    else:
        print(l[i])