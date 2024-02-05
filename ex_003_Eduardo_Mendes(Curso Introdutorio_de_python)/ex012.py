# Faça um programa que receba uma string, com um número de ponto flutuante, e imprima a parte dele que não é inteira
# Ex: 3.14 resposta 14
numero = input('Digite um número de ponto fluatuante: ').split('.')
print(f'Resposta: {numero[1]}')

