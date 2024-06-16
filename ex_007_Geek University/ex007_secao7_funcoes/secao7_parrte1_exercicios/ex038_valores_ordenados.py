"""
Peça ao usuário para digitar dez valores numéricos e ordene por ordem crescente esses valores, 
guardando-os num vetor. 
Ordene o valor assim que ele for digitado. 
Mostre ao final na tela os valores em ordem.
"""
numeros = []
for x in range(1, 11):
    numero = int(input(f'Digite o {x}º valor: '))
    numeros.append(numero)
    print(sorted(numeros))

print(f'Valor final: {sorted(numeros)}')
