selecao_a = input()
ataque_a = int(input())
defesa_a = int(input())
folego_a = int(input())
selecao_b = input()
ataque_b = int(input())
defesa_b = int(input())
folego_b = int(input())
gol_a = gol_b = 0
bool_a = bool_b = True
canseira_a = 1 - ((5 - folego_a)/10)
canseira_b = 1 - ((5 - folego_b)/10)
#turno 1, seleção A ataca, seleção B defende
sorte = int(input())
if sorte == 1:
    ataque_a += 2
    bool_a = False
elif sorte == 2:
    defesa_b += 2
    bool_b = False
print(f'Início de jogo!')
print('1° tempo:')
print(f'{selecao_a} [{gol_a}-{gol_b}] {selecao_b}')
print(f'O time {selecao_a} vem pressionando.')
if ataque_a >= defesa_b:
    gol_a += 1
    print(f'GOOOOOOOOOOOOLLLLLL DO TIME {selecao_a}!!!')
else:
    print(f'O ataque é interrompido! Ótima defesa do time {selecao_b}')
if bool_a == False:
    ataque_a -= 2
    bool_a = True
elif bool_b == False:
    defesa_b -= 2
    bool_b = True
#turno 2, seleção B ataca, seleção A defende
ataque_a *= canseira_a
defesa_a *= canseira_a
ataque_b *= canseira_b
defesa_b *= canseira_b
sorte = int(input())
if sorte == 1:
    ataque_b += 2
    bool_b = False
elif sorte == 2:
    defesa_a += 2
    bool_a = False
print(f'O time {selecao_b} vem pressionando.')
if ataque_b >= defesa_a:
    gol_b += 1
    print(f'GOOOOOOOOOOOOLLLLLL DO TIME {selecao_b}!!!')
else:
    print(f'O ataque é interrompido! Ótima defesa do time {selecao_a}')
if bool_a == False:
    defesa_a -= 2
    bool_a = True
elif bool_b == False:
    ataque_b -= 2
    bool_b = True
#turno 3, seleção B ataca, seleção A defende
ataque_a *= canseira_a
defesa_a *= canseira_a
ataque_b *= canseira_b
defesa_b *= canseira_b
sorte = int(input())
if sorte == 1:
    ataque_b += 2
    bool_b = False
elif sorte == 2:
    defesa_a += 2
    bool_a = False
print('2° tempo:')
print(f'{selecao_a} [{gol_a}-{gol_b}] {selecao_b}')
print(f'O time {selecao_b} vem pressionando.')
if ataque_b >= defesa_a:
    gol_b += 1
    print(f'GOOOOOOOOOOOOLLLLLL DO TIME {selecao_b}!!!')
else:
    print(f'O ataque é interrompido! Ótima defesa do time {selecao_a}')
if bool_a == False:
    defesa_a -= 2
    bool_a = True
elif bool_b == False:
    ataque_b -= 2
    bool_b = True
#turno 4, seleção A ataca, seleção B defende
ataque_a *= canseira_a
defesa_a *= canseira_a
ataque_b *= canseira_b
defesa_b *= canseira_b
sorte = int(input())
if sorte == 1:
    ataque_a += 2
    bool_a = False
elif sorte == 2:
    defesa_b += 2
    bool_b = False
print(f'O time {selecao_a} vem pressionando.')
if ataque_a >= defesa_b:
    gol_a += 1
    print(f'GOOOOOOOOOOOOLLLLLL DO TIME {selecao_a}!!!')
else:
    print(f'O ataque é interrompido! Ótima defesa do time {selecao_b}')
print(f'{selecao_a} [{gol_a}-{gol_b}] {selecao_b}')
if gol_a == gol_b:
    print('Temos um empate! Será decidido em breve nos pênaltis. Fique ligado!')
elif gol_a > gol_b:
    print(f'ACABOOOOU!! O TIME {selecao_a} É O CAMPEÃO!!!')
elif gol_b > gol_a:
    print(f'Fim de jogo! O time {selecao_b} é campeão.')