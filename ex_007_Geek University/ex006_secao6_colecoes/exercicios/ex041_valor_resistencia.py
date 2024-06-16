"""
Faça um programa que calcula a associação em paralelo de dois resistores R1 e R2
fornecidos pelo usuário via teclado. 

O programa fica pedindo estes valores e calculando 
até que o usuário entre com um valor para resistência igual a zero.

R = (R1 * R2) / (R1+ R2)
"""
while True:
    r1 = float(input("Digite o valor de r1[0 para sair]: "))
    if r1 == 0:
        break
    else:
        r2 = float(input("Digite o valor de r2[0 para sair]: "))
        if r2 == 0:
            break
    r = (r1 * r2) / (r1 + r2)
    print(f'O valor total é: {r}')
