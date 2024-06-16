"""
Leia dois vetores de inteiros x e y, cada um com 5 elementos (assuma que o usuário não informa elementos repetidos). 

Calcule e mostre os vetores resultantes em cada caso abaixo:
    • Soma entre e y: soma de cada elemento de com o elemento da mesma posição em y. 
    • Produto entre x ey: multiplicação de cada elemento de como elemento da mesma posição em y. 
    • Diferença entre X e y: todos os elementos de que não existam em y. 
    • Interseção entre x e y: apenas os elementos que aparecem nos dois vetores. 
    • União entre e y: todos os elementos de , e todos os elementos de y que não estão em .
"""
x = []
y = []
for i in range(1, 6):
    numero = int(input(f'Digite o {i}º valor: '))
    x.append(numero)
    
for j in range(1, 6):
    numero = int(input(f'Digite o {j}º valor: '))
    y.append(numero)
      
print(f'A soma dos valores de X + Y é igual a: {sum(x) + sum(y)}')
print(f'O produto dos valroes de X + Y é igual a: {sum(x) * sum(y)}')
print(f'A diferença entre X e Y é: {set(x).difference(set(y))}')
print(f'A interseção entre X e Y é: {set(x).intersection(set(y))}')
print(f'A União entre X e Y é: {set(x).union(set(y))}')
