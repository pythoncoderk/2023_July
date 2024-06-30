n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(n)
# print(l)

l_food = []
l_book = []
l_suit = []
l_other = []

for i in range(n):
    if l[i][0] == 0:
        l_food.append(l[i][1])
    elif l[i][0] == 1:
        l_book.append(l[i][1])
    elif l[i][0] == 2:
        l_suit.append(l[i][1])
    else:
        l_other.append(l[i][1])

food = (sum(l_food) // 100) * 5
book = (sum(l_book) // 100) * 3
suit = (sum(l_suit) // 100) * 2
other = (sum(l_other) // 100) * 1

print(food + book + suit + other)
