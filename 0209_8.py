n = int(input())
l = [input() for i in range(n)]

# print(n)
# print(l)

ball = 0
st = 0

for i in range(n):
    if l[i] == "strike":
        if st >= 2:
            print("out!")
        else:
            print("strike!")
            st += 1
    else:
        if ball >= 3:
            print("fourball!")
        else:
            print("ball!")
            ball += 1