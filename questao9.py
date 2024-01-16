chance = True
favoritismo_br = int(input())
op1 = input()
favoritismo_op1 = int(input())
gol_br = int(input())
gol_op1 = int(input())
if gol_br >= gol_op1:
    if gol_br == gol_op1:
        if favoritismo_br < favoritismo_op1:
            chance = False
            print('Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...')
        else:
            print('No sufoco, o Brasil conseguiu ganhar!!!')
    elif gol_br > gol_op1:
        print('Quem é que segura o Brasil???')
    if chance == True:
        if gol_br - gol_op1 == 1:
            favoritismo_br += 10
        elif gol_br - gol_op1 == 2:
            favoritismo_br += 20
        elif (gol_br - gol_op1) >= 3:
            favoritismo_br += 30
        op2 = input()
        favoritismo_op2 = int(input())
        gol_br = int(input())
        gol_op2 = int(input())
        if gol_br >= gol_op2:
            if gol_br == gol_op2:
                if favoritismo_br < favoritismo_op2:
                    chance = False
                    print('Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...')
                else:
                    print('No sufoco, o Brasil conseguiu ganhar!!!')
            elif gol_br > gol_op2:
                print('Quem é que segura o Brasil???')
            if chance == True:
                if gol_br - gol_op2 == 1:
                    favoritismo_br += 10
                elif gol_br - gol_op2 == 2:
                    favoritismo_br += 20
                elif (gol_br - gol_op2) >= 3:
                    favoritismo_br += 30
                op3 = input()
                favoritismo_op3 = int(input())
                gol_br = int(input())
                gol_op3 = int(input())
                if gol_br >= gol_op3:
                    if gol_br == gol_op3:
                        if favoritismo_br < favoritismo_op3:
                            chance = False
                            print('Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...')
                        else:
                            print('No sufoco, o Brasil conseguiu ganhar!!!')
                    elif gol_br > gol_op3:
                        print('Quem é que segura o Brasil???')
                    if chance == True:
                        if gol_br - gol_op3 == 1:
                            favoritismo_br += 10
                        elif gol_br - gol_op3 == 2:
                            favoritismo_br += 20
                        elif (gol_br - gol_op3) >= 3:
                            favoritismo_br += 30
                        op4 = input()
                        favoritismo_op4 = int(input())
                        if favoritismo_br < favoritismo_op4:
                            print(f'O nosso Brasil foi vice, não conseguindo bater a seleção dx {op4} na simulação')
                        else:
                            print(f'O BRASIL VAI SER HEXAAAAAAAA')
                else:
                    print(f'Infelizmente essa seleção dx {op3} era muito forte para o Brasil.')
        else:
            print(f'Infelizmente essa seleção dx {op2} era muito forte para o Brasil.')
else:
    print(f'Infelizmente essa seleção dx {op1} era muito forte para o Brasil.')
