"""
Em uma eleição presidencial existem quatro candidatos.
Os votos são informados por meio de código. Os códigos utilizados são:

1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:
O total de votos para cada candidato; X
O total de votos nulos; X
O total de votos em branco; X
A percentagem de votos nulos sobre o total de votos; X
A percentagem de votos em branco sobre o total de votos.  X
Para finalizar o conjunto de votos tem-se o valor zero.
"""
voto1 = []
voto2 = []
voto3 = []
voto4 = []
voto_nulo = []
voto_em_branco = []
while True:
    codigos = int(input('''
===== Vote abaixo com números =====
1 - James Felipe
2 - Antony Jobson
3 - Alessa Magalhaes
4 - Surubim 
5- Voto nulo
6 - Voto em Branco

voto = '''))
    if codigos == 0:
        break
    elif codigos == 1:
        voto1.append(codigos)
    elif codigos == 2:
        voto2.append(codigos)
    elif codigos == 3:
        voto3.append(codigos)
    elif codigos == 4:
        voto4.append(codigos)
    elif codigos == 5:
        voto_nulo.append(codigos)
    elif codigos == 6:
        voto_em_branco.append(codigos)                
print(f'Total de votos do candidato James Felipe: {len(voto1)}')
print(f'Total de votos do candidato Antony Jobson: {len(voto2)}')
print(f'Total de votos da candidata Alessa Magalhaes: {len(voto3)}')
print(f'Total de votos do candidato Surubim: {len(voto4)}')
print(f'Total de votos nulos: {len(voto_nulo)}')
print(f'Total de votos em branco: {len(voto_em_branco)}')
total_geral = [len(voto1), len(voto2), len(voto3), len(voto4)]
total_geral = sum(total_geral)
percetagem_nulo_sobre_tot = total_geral - (total_geral * len(voto_nulo) / 100)
percetagem_branco_sobre_tot = total_geral - (total_geral * len(voto_em_branco) / 100)
print(f'Percentagem de votos nulos sobre o total de votos: {percetagem_nulo_sobre_tot}%')
print(f'Percentagem de votos branco sobre o total de votos: {percetagem_branco_sobre_tot}%')
