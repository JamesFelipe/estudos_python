"""
Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999).
Gere outro número formado pelos dígitos invertidos do número lido. Exemplo:

    NúmeroLido = 123
    NumeroGerado = 321
"""
numero = int(input('Digite um número de três digitos: '))
print(f'\tNúmero lido: {numero}')
print(f'\tNúmero gerado: {str(numero)[::-1]}')
