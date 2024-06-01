s = input()
n = int(input())
l = list(map(str, input().split()))

# print(s)
# print(n)
# print(l)

if s in l:
    print("Yes")
else:
    print("No")