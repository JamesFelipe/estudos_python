#importação da biblioteca
from math import sqrt

while True:
    try:
        #entrada dos valores
        a = int(input('Digite um valor inteiro: '))
        b = int(input('Digite outro valor inteiro: '))
        # formula para culcular o valor da hipotenusa
        hipotenusa = sqrt((a*a) + (b*b)) 
    except ValueError:
        print('Apenas valores inteiros são aceitos... Digite novamente....')
    else:
        print(f'Valor da hipotenusa: {hipotenusa:.2f}')
        break
