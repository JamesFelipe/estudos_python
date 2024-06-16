"""
Faça um programa que leia dois vetores de 10 elementos. 
Crie um vetor que seja a união entre os 2 vetores anteriores, 
ou seja, que contém os números dos dois vetores. 
Não deve conter números repetidos.
"""
vetor1 = []
vetor2 = []
for i in range(1, 11):
    vetor = int(input('Digite um valor: '))
    vetor1.append(vetor)

for j in range(1, 11):
    vetor = int(input('Digite um valor: '))
    vetor2.append(vetor)
    
uniao = set(vetor1).union(vetor2)
print(f'Vetor 1: {vetor1}\nVetor2: {vetor2}')
print(f'União dos vetores: {uniao}')
