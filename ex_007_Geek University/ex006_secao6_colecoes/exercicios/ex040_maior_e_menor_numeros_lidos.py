"""
Elabore um programa que faça leitura de vários números inteiros,
até que se digite um número negativo. 

O programa tem que retornar o maior e o menor número lido.
"""
maior = 0
menor = 9999
while True:
    numeros = int(input("Digite um valor inteiro[valor negativo para sair]: "))
    if numeros < 0:
        break
    
    if numeros > maior:
        maior = numeros
    if  numeros < menor:
        menor = numeros

print(f'O maior número digitado foi: {maior} e o menor número digitado foi: {menor}')
