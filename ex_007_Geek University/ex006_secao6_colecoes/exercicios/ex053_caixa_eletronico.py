"""
Escreva um programa que receba como entrada o valor do saque realizado 
pelo cliente de um banco e retorne quantas notas de cada valor serão 
necessárias para atender ao saque com a menor quantidade de notas possível. 

Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real.
"""
valor = int(input('Digite quanto vocÊ quer sacar: '))
total = valor
cedula = 100
total_cedula  = 0
while True:
    if total >= cedula:
        total -=cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R${cedula}')
        if cedula == 100:
            cedula = 50
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break
