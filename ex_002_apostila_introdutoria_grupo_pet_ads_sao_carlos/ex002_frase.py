"""
Escreva um programa que solicite uma frase ao usuário e escreva a frase toda em maiúscula e
sem espaços em branco.
"""
frase = input('Digite uma frase: ').strip().upper()
frase = frase.split()
junto = ''.join(frase)
print(junto)
