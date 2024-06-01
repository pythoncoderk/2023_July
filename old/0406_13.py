n = int(input())
l = [int(input()) for i in range(n)]
m = int(input())
l2 = [int(input()) for i in range(m)]

# print(n)
# print(l)
# print(m)
# print(l2)

a_or_b = "a"
for i in range(1, 32):
    if i in l and i in l2:
        if a_or_b == "a":
            print("A")
            a_or_b = "b"
        else:
            print("B")
            a_or_b = "a"
    elif i in l:
        print("A")
    elif i in l2:
        print("B")
    else:
        print("x")

