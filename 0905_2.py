h = int(input())

paiza = 1
monster = 1

turn = True
paiza_damage = 0
monster_damage = 0
count = 1
paiza_l = []
monster_l = []
while True:
    if count == 1 or count == 2:
        monster_damage += 1
        count += 1
        turn = False
        monster_l.append(1)
    else:
        monster_damage += paiza_l[-1] + paiza_l[-2]
        count += 1
        turn = False
        monster_l.append(paiza_l[-1] + paiza_l[-2])

        if count == 1 or count == 2:
            paiza_damage += 1
            count += 1
            turn = True
            paiza_l.append(1)
        else:

