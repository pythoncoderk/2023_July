n = int(input())
l = [input() for i in range(n)]

# print(n)
# print(l)

l = set(l)

if len(l) == 3 or len(l) == 1:
    print("draw")
elif "rock" not in l:
    print("scissors")
elif "paper" not in l:
    print("rock")
elif "scissors" not in l:
    print("paper")
else:
    print("draw")