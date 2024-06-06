try:
    n = int(input('Digit e um valor inteiro (entre 1000 a 999): '))
    string = str(n) # convertendo um número inteiro para string
except ValueError:
    print('Apenas valores inteiros são aceitos...')
# Forma 1
else:
    for numero in string:
        print(numero)

# forma 2
"""print(f'{string[0]}')
print(f'{string[1]}')
print(f'{string[2]}')
print(f'{string[3]}')"""

