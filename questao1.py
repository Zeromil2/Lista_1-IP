#n = nome do jogador
n = input()
if n == 'Alisson' or n == 'Ederson' or n == 'Weverton':
  print(f'{n} foi convocado e jogará como goleiro!')
elif n == 'Daniel Alves' or n == 'Danilo' or n == 'Alex Sandro' or n == 'Alex Telles':
  print(f'{n} foi convocado e jogará como lateral!')
elif n == 'Marquinhos' or n == 'Thiago Silva' or n == 'Éder Militão' or n == 'Bremer':
    print(f'{n} foi convocado e jogará como zagueiro!')
elif n == 'Casemiro' or n == 'Fabinho' or n == 'Fred' or n == 'Bruno Guimarães' or n == 'Lucas Paquetá' or n == 'Everton Ribeiro':
    print(f'{n} foi convocado e jogará como meia!')
elif n == 'Neymar' or n == 'Raphinha' or n == 'Vini Jr.' or n == 'Antony' or n == 'Richarlison' or n == 'Rodrygo' or n == 'Pedro' or n == 'Gabriel Jesus' or n == 'Gabriel Martinelli':
    print(f'{n} foi convocado e jogará como atacante!')
else:
    print(f'{n} não foi convocado, mas quem sabe na próxima?')