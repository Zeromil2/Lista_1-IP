nome = input()
disp = int(input())
if disp >= 85:
    posicao = input()
    chutes_passes = int(input())
elif 50 <= disp < 85:
    des_ult_jogo = int(input())
else:
    des_ult_treino = int(input())
if disp >= 85:
    if posicao == 'atacante':
        if chutes_passes > 10:
            print(f'{nome} esta com um bom desempenho')
        elif chutes_passes <= 10:
            print(f'{nome} pode melhorar, coloque-o no segundo tempo')
    else:
        if chutes_passes >= 20:
            print(f'{nome} esta com um bom desempenho')
        elif chutes_passes < 20:
            print(f'{nome} pode melhorar, nao entrara no primeiro tempo')
elif 50 <= disp < 85:
    if des_ult_jogo > 80:
        print(f'Jogador {nome} pode ser escalado')
    else:
        print(f'Analisar o desempenho do {nome} na partida')
else:
    if des_ult_treino > 70:
        print(f'Voce deve colocar {nome} para treinar mais')
    else:
        print(f'{nome} nao deveria estar na copa')