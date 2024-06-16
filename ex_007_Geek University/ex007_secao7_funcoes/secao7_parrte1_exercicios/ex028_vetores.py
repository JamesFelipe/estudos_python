"""
Leia 10 números inteiros e armazene em um vetor v. Crie dois novos vetores v1 e v2.
Copie os valores ímpares de v para v1, e os valores pares de v para v2. Note que cada
um dos vetores v1 e v2 têm no máximo 10 elementos, mas nem todos os elementos são
utilizados. No final escreva os elementos UTILIZADOS de »1 e v2.
"""
v = []
v1 = []
v2 = []
for i in range(1, 11):
    numero = int(input(f'Digite o {i}º número: '))
    v.append(numero)
    

for i in v:
    if i % 2 == 0:
        v2.append(i)
    elif i % 2 == 1:
        v1.append(i)
print(f'Os valores ímpares em v1: {v1}')
print(f'Os valores pares em v2: {v2}')
