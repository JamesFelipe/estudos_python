# Faça um programa que receba um número inteiro maior do que 1, 
# e verifique se o número fornecido é primo ou não.
num = int(input("Digite um valor inteiro: "))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
if tot == 2:
    print('PRIMO')
else:
    print('NÃO é PRIMO')
