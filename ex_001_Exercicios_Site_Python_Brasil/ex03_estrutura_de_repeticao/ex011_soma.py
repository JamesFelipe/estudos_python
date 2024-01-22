# Altere o programa anterior para mostrar no final a soma dos números.# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
soma = 0
numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))
print(f'Os números que estão entre {numero1} e {numero2} são: ', end=' ')
for i in range(numero1, numero2):
    soma += i
    print(i, end=' ')
print(f'\nE a soma desses valores dá: {soma}')
