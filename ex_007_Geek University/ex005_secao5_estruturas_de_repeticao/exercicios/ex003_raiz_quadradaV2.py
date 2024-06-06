"""
Leia um numero real. Se o número for positivo imprima a raiz quadrada. Do contrário,
imprima o numero ao quadrado.
"""
numero = float(input('Digite um valor: '))
if numero > 0:
    print(f'A raiz de {numero} é: {numero ** (1/2)}')
elif numero < 0:
    print(f'O número {numero} ao quadrado é: {abs(numero * 2)}')
