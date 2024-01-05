x = int(input())
if x >= 35:
    print("extremely hot day")
elif x >= 30:
    print("hot summer day")
elif x >= 25:
    print("summer day")
elif x < 0:
    print("ice day")
else:
    print("normal day")