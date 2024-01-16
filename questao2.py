#sv = seleção vencedora, sp = seleção perdedora, a = aposta, p = probabilidade, r = resultado
sv = input()
sp = input()
a = int(input())
p = float(input())
r = input()
if p >= 0.5:
    print('Pedro, você está proibido de apostar nos favoritos, só em zebra, lembra?')
else:
    valor = int(a * (1 + (0.5 - p)** 2 * 100))
    if r == 'Ganhou':
        if 0.4 < p < 0.5:
            print(f'Não foi um palpite tão arriscado, todos sabiam que {sv} não estava muito atrás de {sp}')
            print(f'Parabéns, você apostou R${a} e recebeu R${valor} nessa aposta')
        elif 0.3 < p <= 0.4:
            print(f'Eu pensava que {sp} iria ganhar, mas nunca duvidei que a {sv} pudesse ganhar essa partida')
            print(f'Parabéns, você apostou R${a} e recebeu R${valor} nessa aposta')
        elif 0.2 < p <= 0.3:
            print(f'Uau! que jogo foi esse?? {sv} surpreendeu a todos nós…')
            print(f'Parabéns, você apostou R${a} e recebeu R${valor} nessa aposta')
        elif 0.1 < p <= 0.2:
            print(f'Essa é a copa das zebras?? O impossível aconteceu hoje nessa partida, como que {sv} ganhou de {sp}, alguém me explica?')
            print(f'Parabéns, você apostou R${a} e recebeu R${valor} nessa aposta')
        elif p <= 0.1:
            print(f'PEDROOOOO, você tá rico!! ninguém, absolutamente ninguém apostou na {sv}, somente você!')
            print(f'Parabéns, você apostou R${a} e recebeu R${valor} nessa aposta')
    elif r == 'Perdeu':
        print('Pedro, infelizmente você está no fundo do poço, se endividou completamente e não temos o que fazer…')
        print(f'Você poderia ter ganhado R${valor}, mas perdeu R${a}')
