"""
Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""
altura = float(input('Digite sua altura: '))
ideal_homem = (72.7 * altura) - 58
ideal_mulher = ((62.1 * altura) - 44.7)
print(f'Sua altura é: {altura} e seu peso ideal é: {ideal_homem:.2f} se você for homem')
print(f'Sua altura é: {altura} e seu peso ideal é: {ideal_mulher:.2f} se você for mulher')
