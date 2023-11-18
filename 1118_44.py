import re

n = input()
if n == "5":
    print(re.sub("[5]", "A", n))
elif n == "4":
    print(re.sub("[4]", "B", n))
elif n == "3":
    print(re.sub("[3]", "C", n))
elif n == "2":
    print(re.sub("[2]", "D", n))
elif n == "1":
    print(re.sub("[1]", "E", n))