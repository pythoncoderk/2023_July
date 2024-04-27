n = int(input())
l = [input() for i in range(n)]

# print(n)
# print(l)

l = set(l)
# l = list(l)

if len(l) == 1:
    print("draw")
elif "rock" not in l:
    print("scissors")
elif "scissors" not in l:
    print("paper")
elif "paper" not in l:
    print("rock")
else:
    print("draw")

