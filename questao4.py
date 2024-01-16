n1 = input()
b1 = input()
carisma1 = input()
emocao1 = int(input())
n2 = input()
b2 = input()
carisma2 = input()
emocao2 = int(input())
if b1 == 'PROOOO FUNDO DO GOOOL':
    emocao1 += 15
elif b1 =='EU QUERO É GRITAR GOL':
    emocao1 -= 10
elif b1 == 'VOCÊ. É. RIDÍCULO':
    emocao1 += 18
elif b1 == 'QUEM SABE NA BOLA PARADA':
    emocao1 -= 5
else:
    emocao1 += 10
if b2 == 'PROOOO FUNDO DO GOOOL':
    emocao2 += 15
elif b2 =='EU QUERO É GRITAR GOL':
    emocao2 -= 10
elif b2 == 'VOCÊ. É. RIDÍCULO':
    emocao2 += 18
elif b2 == 'QUEM SABE NA BOLA PARADA':
    emocao2 -= 5
else:
    emocao2 += 10
if carisma1 == 'sim':
    carisma1 = True
    emocao1 += 10
elif carisma1 == 'nao':
    carisma1 = False
if carisma2 == 'sim':
    carisma2 = True
    emocao2 += 10
elif carisma2 =='nao':
    carisma2 = False
if emocao1 > emocao2:
    print(f'O(a) narrador(a) escolhido(a) é {n1}! Ele(a) será um(a) sucessor(a) digno(a) para o grande Galvão.')
elif emocao2 > emocao1:
    print(f'O(a) narrador(a) escolhido(a) é {n2}! Ele(a) será um(a) sucessor(a) digno(a) para o grande Galvão.')