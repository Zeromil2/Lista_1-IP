saldo1 = saldo2 = saldo3 = 0
selecao1 = input()
resultado1_jogo1 = input()
if resultado1_jogo1 == 'Ganhou':
    saldo1 += 3
elif resultado1_jogo1 == 'Empatou':
    saldo1 += 1
resultado1_jogo2 = input()
if resultado1_jogo2 == 'Ganhou':
    saldo1 += 3
elif resultado1_jogo2 == 'Empatou':
    saldo1 += 1
selecao2 = input()
resultado2_jogo1 = input()
if resultado2_jogo1 == 'Ganhou':
    saldo2 += 3
elif resultado2_jogo1 == 'Empatou':
    saldo2 += 1
resultado2_jogo2 = input()
if resultado2_jogo2 == 'Ganhou':
    saldo2 += 3
elif resultado2_jogo2 == 'Empatou':
    saldo2 += 1
selecao3 = input()
resultado3_jogo1 = input()
if resultado3_jogo1 == 'Ganhou':
    saldo3 += 3
elif resultado3_jogo1 == 'Empatou':
    saldo3 += 1
resultado3_jogo2 = input()
if resultado3_jogo2 == 'Ganhou':
    saldo3 += 3
elif resultado3_jogo2 == 'Empatou':
    saldo3 += 1
if saldo1 > saldo3 and saldo2 > saldo3:
    print(f'Parabéns aos países {selecao1} e {selecao2}, vocês estão classificados para as oitavas de finais!!!')
elif saldo1 > saldo2 and saldo3 > saldo2:
    print(f'Parabéns aos países {selecao1} e {selecao3}, vocês estão classificados para as oitavas de finais!!!')
elif saldo2 > saldo1 and saldo3 > saldo1:
    print(f'Parabéns aos países {selecao2} e {selecao3}, vocês estão classificados para as oitavas de finais!!!')