"""
Faça um programa que possua um vetor denominado A que armazene 6 números intei-
ros. O programa deve executar os seguintes passos: 

(a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
(b) Armazene em uma variável inteira (simples) a soma entre os valores das posições
A(O), A[1] e [5] do vetor e mostre na tela esta soma.

(c) Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.
(d) Mostre na tela cada valor do vetor A, um em cada linha.
"""
A = [1,0,5, -2, -5, 7.]
print(f'A: {A}')
B = A[0] + A[1] + A[5]
print(f'B: {B}')
A[4] = 100
print(f'C: {A}')
for i in A:
    print(i)
