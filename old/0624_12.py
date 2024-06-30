n = int(input())
l = [input() for i in range(n)]

# print(n)
# print(l)


rock = l.count("rock")
scissors = l.count("scissors")
paper = l.count("paper")

# print(rock)
# print(scissors)
# print(paper)

if rock >= 1 and scissors >= 1 and paper >= 1:
    print("draw")
elif rock == 0 and scissors != 0 and paper != 0:
    print("scissors")
elif rock != 0 and scissors != 0 and paper == 0:
    print("rock")
elif rock != 0 and scissors == 0 and paper != 0:
    print("paper")
else:
    print("draw")