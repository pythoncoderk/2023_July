n = int(input())
l = [int(input()) for i in range(n)]

# print(n)
# print(l)

for i in range(n-1):
    if l[i] == l[i+1]:
        print("stay")
    elif l[i] > l[i+1]:
        print(f"down {l[i] - l[i+1]}")
    else:
        print(f"up {l[i+1] - l[i]}")