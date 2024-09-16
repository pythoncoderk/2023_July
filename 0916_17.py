h = int(input())

paiza = []
monster = []
p_count = 1
m_count = 1
hit = "p"
while sum(paiza) < h:
    if hit == "p":
        if p_count == 1 or p_count == 2:
            monster.append(1)
            hit = "m"
            p_count += 1
        else:
            monster.append(paiza[-1] + paiza[-2])
            hit = "m"
            p_count += 1
    else:
        if m_count == 1 or m_count == 2:
            paiza.append(1)
            hit = "p"
            m_count += 1
        else:
            paiza.append(monster[-1] * 2 + monster[-2])
            hit = "p"
            m_count += 1

print(m_count)