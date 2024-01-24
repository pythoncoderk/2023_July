n = int(input())
l = [input() for i in range(n)]
# print(l)
paper = 0
rock = 0
scissors = 0

for i in l:
    if i == "paper":
        paper += 1
    elif i == "rock":
        rock += 1
    elif i == "scissors":
        scissors += 1

if paper >= 1 and rock >= 1 and scissors >= 1:
    print("draw")
elif l.count("paper") == n:
    print("draw")
elif l.count("rock") == n:
    print("draw")
elif l.count("scissors") == n:
    print("draw")
elif paper == 0:
    print("rock")
elif rock == 0:
    print("scissors")
elif scissors == 0:
    print("paper")