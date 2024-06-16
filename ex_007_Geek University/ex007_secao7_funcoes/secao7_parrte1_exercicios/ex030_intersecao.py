"""
Faça um programa que leia dois vetores de 10 elementos. 
Crie um vetor que seja a intersecção entre os 2 vetores anteriores,
ou seja, que contém apenas os números que estão em ambos os vetores. 
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
    
intersecao = set(vetor1).intersection(vetor2)
print(f'Valores que estão em ambos os vetores: {intersecao}')
