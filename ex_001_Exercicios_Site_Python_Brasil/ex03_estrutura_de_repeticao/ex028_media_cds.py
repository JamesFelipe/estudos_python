# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs 
# e o valor médio gasto em cada um deles. 
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.
total = []
cds = int(input('Digite quantos cds você tem: '))
for i in range(1, cds + 1):
    preco = float(input(f'Digite o preço do cd {i}: '))
    total.append(preco)

print(f'Você pagou em media {sum(total) / cds:.2f}R$')
