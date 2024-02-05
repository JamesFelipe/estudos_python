# faça um programa que dada a entrada de uma lista ele faça o cálculo acumulativo da mesma:
# Exemplo de entrada: [1, 2, 3, 4]
# Exemplo de saída: [1, 3, 6, 10]
lista1 = [1, 2, 3, 4]
lista2 = [1, 3, 6, 10] 
soma = soma2 = 0
for i in lista1:
    soma += i
    
for j in lista2:
    soma2 += j
    
print(f'A soma dos valores da lista1 é: {soma}')
print(f'A soma dos valores da lista2 é: {soma2}')