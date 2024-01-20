h, w, n = map(int, input().split())
l1 = [list(map(int, input().split())) for i in range(h)]
game_count = int(input())
l2 = [list(map(int, input().split())) for i in range(game_count)]

print(h, w, n)
print(l1)
print(game_count)
print(l2)

players = []
for i in range(n):
    players.append([])
print(players)

