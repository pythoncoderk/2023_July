n = input()
x = n.count("_")
y = n.count("-")
if x > y or x == y:
    print(n.replace("-", "_"))
elif x < y:
    print(n.replace("_", "-"))