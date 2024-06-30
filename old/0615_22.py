n = list(input())

one = n[:3]
two = n[1:]

# print(one)
# print(two)

if one.count(one[0]) >= 3 or two.count(two[0]) >= 3:
    print("Yes")
else:
    print("No")