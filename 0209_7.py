n = int(input())
l = [input() for i in range(n)]

st = 0
for i in range(n):
    if l[i] == "strike":
        if st >= 2:
            st += 1
            print("out!")
        else:
            print("strike!")
            st += 1
    else:
        print(l[i])