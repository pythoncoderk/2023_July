x, y = map(str, input().split())

# print(x, y)

bob = 0
for i in range(len(x)):
    bob += int(x[i])
bob = str(bob)[-1]
bob = int(bob)

ali = 0
for i in range(len(y)):
    ali += int(y[i])
ali = str(ali)[-1]
ali = int(ali)

# print(bob)
# print(ali)

if bob == ali:
    print("Draw")
elif bob > ali:
    print("Bob")
else:
    print("Alice")