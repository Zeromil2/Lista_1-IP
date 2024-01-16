selecao1 = input()
selecao2 = input()
gol_s1 = gol_s2 = 0
chute_s1 = input()
if chute_s1 == 'Gol':
    gol_s1 += 1
chute_s2 = input()
if chute_s2 == 'Gol':
    gol_s2 += 1
chute_s1 = input()
if chute_s1 == 'Gol':
    gol_s1 += 1
chute_s2 = input()
if chute_s2 == 'Gol':
    gol_s2 += 1
chute_s1 = input()
if chute_s1 == 'Gol':
    gol_s1 += 1
chute_s2 = input()
if chute_s2 == 'Gol':
    gol_s2 += 1
if abs(gol_s1 - gol_s2) < 3:
    chute_s1 = input()
    if chute_s1 == 'Gol':
        gol_s1 += 1
if abs(gol_s1 - gol_s2) < 3 and (gol_s1 - gol_s2) != -2:
    chute_s2 = input()
    if chute_s2 == 'Gol':
        gol_s2 += 1
if abs(gol_s1 - gol_s2) < 2:
    chute_s1 = input()
    if chute_s1 == 'Gol':
        gol_s1 += 1
if abs(gol_s1 - gol_s2) < 2 and (gol_s1 - gol_s2) != -1:
    chute_s2 = input()
    if chute_s2 == 'Gol':
        gol_s2 += 1
if gol_s1 > gol_s2:
    print(f'{selecao1} vence a disputa de pênaltis por {gol_s1} a {gol_s2} e avança de fase!')
elif gol_s2 > gol_s1:
    print(f'{selecao2} vence a disputa de pênaltis por {gol_s2} a {gol_s1} e avança de fase!')
else:
    print(f'Ambas as seleções terminaram com {gol_s1} gols, mas o desempate vai ficar para outro dia.')