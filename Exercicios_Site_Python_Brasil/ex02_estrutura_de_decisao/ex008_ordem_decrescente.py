# Faça um Programa que leia três números e mostre-os em ordem decrescente.
numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))
numero3 = int(input('Digite o terceiro valor: '))
numeros = [numero1, numero2, numero3]
print(f'Os valores em ordem descresente são: {sorted(numeros, reverse=True)}')
