"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.

As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a 
participação da pessoa no crime. 

Se a pessoa responder positivamente a 2 questões ela deve ser classificada
como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".
"""
cont = 0
print('Responda com S - Sim ou N - Não...')
p1 = input("Telefonou para a vítima? ").strip().lower()
if p1 == 's':
    cont += 1
p2 = input("Esteve no local do crime? ").strip().lower()
if p2 == 's':
    cont += 1
p3 = input("Mora perto da vítima? ").strip().lower()
if p3 == 's':
    cont += 1
p4 = input("Devia para a vítima? ").strip().lower()
if p4 == 's':
    cont += 1
p5 = input("Já trabalhou com a vítima? ").strip().lower()
if p5 == 's':
    cont += 1
if cont == 2:
    print('Suspeita')
elif cont >= 3 and cont <= 4:
    print('Cúmplice')
elif cont == 5:
    print('Assasino')
else:
    print('Inocente')
    