maior = 0
melhor = medio = pior = ''
jogador1 = input()
bola_area1 = int(input())
chute1 = int(input())
gol1 = int(input())
taxa1 = gol1/chute1
jogador2 = input()
bola_area2 = int(input())
chute2 = int(input())
gol2 = int(input())
taxa2 = gol2/chute2
jogador3 = input()
bola_area3 = int(input())
chute3 = int(input())
gol3 = int(input())
taxa3 = gol3/chute3
if bola_area1 > bola_area2 and bola_area1 > bola_area3:
    maior = bola_area1
    melhor = jogador1
    if bola_area2 > bola_area3:
        medio = jogador2
        pior = jogador3
    elif bola_area3 > bola_area2:
        medio = jogador3
        pior = jogador2
    else:
        if taxa2 > taxa3:
            medio = jogador2
            pior = jogador3
        elif taxa3 > taxa2:
            medio = jogador3
            pior = jogador2
elif bola_area2 > bola_area1 and bola_area2 > bola_area3:
    maior = bola_area2
    melhor = jogador2
    if bola_area1 > bola_area3:
        medio = jogador1
        pior = jogador3
    elif bola_area3 > bola_area1:
        medio = jogador3
        pior = jogador1
    else:
        if taxa1 > taxa3:
            medio = jogador1
            pior = jogador3
        elif taxa3 > taxa1:
            medio = jogador3
            pior = jogador1
elif bola_area3 > bola_area1 and bola_area3 > bola_area2:
    maior = bola_area3
    melhor = jogador3
    if bola_area1 > bola_area2:
        medio = jogador1
        pior = jogador2
    elif bola_area2 > bola_area1:
        medio = jogador2
        pior = jogador1
    else:
        if taxa1 > taxa2:
            medio = jogador1
            pior = jogador2
        elif taxa2 > taxa1:
            medio = jogador2
            pior = jogador1
elif bola_area1 == bola_area2 > bola_area3:
    maior = bola_area1
    print(f'Tite está mais indeciso do que nunca!')
    pior = jogador3
    if taxa1 > taxa2:
        melhor = jogador1
        medio = jogador2
    elif taxa2 > taxa1:
        melhor = jogador2
        medio = jogador1
elif bola_area1 == bola_area3 > bola_area2:
    maior = bola_area1
    print(f'Tite está mais indeciso do que nunca!')
    pior = jogador2
    if taxa1 > taxa3:
        melhor = jogador1
        medio = jogador3
    elif taxa3 > taxa1:
        melhor = jogador3
        medio = jogador1
elif bola_area2 == bola_area3 > bola_area1:
    maior = bola_area2
    print(f'Tite está mais indeciso do que nunca!')
    pior = jogador1
    if taxa2 > taxa3:
        melhor = jogador2
        medio = jogador3
    elif taxa3 > taxa2:
        melhor = jogador3
        medio = jogador2
elif bola_area1 == bola_area2 == bola_area3:
    maior = bola_area1
    print(f'Tite está mais indeciso do que nunca!')
    if taxa1 > taxa2 and taxa1 > taxa3:
        melhor = jogador1
        if taxa2 > taxa3:
            medio = jogador2
            pior = jogador3
        elif taxa3 > taxa2:
            medio = jogador3
            pior = jogador2
    elif taxa2 > taxa1 and taxa2 > taxa3:
        melhor = jogador2
        if taxa1 > taxa3:
            medio = jogador1
            pior = jogador3
        elif taxa3 > taxa1:
            medio = jogador3
            pior = jogador1
    elif taxa3 > taxa1 and taxa3 > taxa2:
        melhor = jogador3
        if taxa1 > taxa2:
            medio = jogador1
            pior = jogador2
        elif taxa2 > taxa1:
            medio = jogador2
            pior = jogador1
print(melhor)
print(medio)
print(pior)
print(f'Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…')
if maior <= 10:
    print(f'{melhor}?! Sei não hein Galvão…')
else:
    print(f'{melhor}! Dessa vez o hexa vem pra casa!!')