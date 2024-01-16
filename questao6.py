ano = int(input())
selecao1 = input()
v1 = int(input())
e1 = int(input())
pontos_s1 = (v1 * 3) + e1
selecao2 = input()
v2 = int(input())
e2 = int(input())
pontos_s2 = (v2 * 3) + e2
selecao3 = input()
v3 = int(input())
e3 = int(input())
pontos_s3 = (v3 * 3) + e3
tipo_consulta = input()
if tipo_consulta == 'Critério Geral':
    print(f'A classificação na copa de {ano} foi:')
    if pontos_s1 > pontos_s2 > pontos_s3:
        print(f'{selecao1} - {pontos_s1}')
        print(f'{selecao2} - {pontos_s2}')
        print(f'{selecao3} - {pontos_s3}')
    elif pontos_s1 > pontos_s3 > pontos_s2:
        print(f'{selecao1} - {pontos_s1}')
        print(f'{selecao3} - {pontos_s3}')
        print(f'{selecao2} - {pontos_s2}')
    elif pontos_s2 > pontos_s1 > pontos_s3:
        print(f'{selecao2} - {pontos_s2}')
        print(f'{selecao1} - {pontos_s1}')
        print(f'{selecao3} - {pontos_s3}')
    elif pontos_s2 > pontos_s3 > pontos_s1:
        print(f'{selecao2} - {pontos_s2}')
        print(f'{selecao3} - {pontos_s3}')
        print(f'{selecao1} - {pontos_s1}')
    elif pontos_s3 > pontos_s2 > pontos_s1:
        print(f'{selecao3} - {pontos_s3}')
        print(f'{selecao2} - {pontos_s2}')
        print(f'{selecao1} - {pontos_s1}')
    elif pontos_s3 > pontos_s1 > pontos_s2:
        print(f'{selecao3} - {pontos_s3}')
        print(f'{selecao1} - {pontos_s1}')
        print(f'{selecao2} - {pontos_s2}')
elif tipo_consulta == 'Ordem Lexicográfica':
    print(f'O times por ordem Lexicográfica da copa de {ano} são:')
    if selecao1 < selecao2 < selecao3:
        print(f'{selecao1} - {pontos_s1}')
        print(f'{selecao2} - {pontos_s2}')
        print(f'{selecao3} - {pontos_s3}')
    elif selecao1 < selecao3 < selecao2:
        print(f'{selecao1} - {pontos_s1}')
        print(f'{selecao3} - {pontos_s3}')
        print(f'{selecao2} - {pontos_s2}')
    elif selecao2 < selecao1 < selecao3:
        print(f'{selecao2} - {pontos_s2}')
        print(f'{selecao1} - {pontos_s1}')
        print(f'{selecao3} - {pontos_s3}')
    elif selecao2 < selecao3 < selecao1:
        print(f'{selecao2} - {pontos_s2}')
        print(f'{selecao3} - {pontos_s3}')
        print(f'{selecao1} - {pontos_s1}')
    elif selecao3 < selecao2 < selecao1:
        print(f'{selecao3} - {pontos_s3}')
        print(f'{selecao2} - {pontos_s2}')
        print(f'{selecao1} - {pontos_s1}')
    elif selecao3 < selecao1 < selecao2:
        print(f'{selecao3} - {pontos_s3}')
        print(f'{selecao1} - {pontos_s1}')
        print(f'{selecao2} - {pontos_s2}')