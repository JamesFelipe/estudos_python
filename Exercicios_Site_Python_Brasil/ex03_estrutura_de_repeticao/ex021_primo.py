# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.
# Código Curso em vídeo modificado
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        tot += 1

if tot == 2:
    print(f'O número {num} é primo')
else:
    print(f'O número {num} não é primo')
