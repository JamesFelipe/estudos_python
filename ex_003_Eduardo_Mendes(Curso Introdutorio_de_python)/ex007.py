# Faça um programa que receba uma string e responda se ela tem alguma vogal, se sim, quais são?
# E também diga se ela é uma frase ou não
# Código chatgpt
string = input('Digite uma sring: ')
vogais = []
eh_frase = False
for letra in string:
    if letra.lower() in 'aeiou':
        if letra.lower() not in vogais:
            vogais.append(letra.lower())
    if letra == '.':
        eh_frase = True

if vogais:
    print('Vogais na string: ', ' ,'.join(vogais))
else:
    print('A string não contém vogais')

if eh_frase:
    print('A string é uma frase')
else:
    print('A string não é uma frase')
