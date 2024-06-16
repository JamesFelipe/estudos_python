"""
Considere um vetor A com 11 elementos onde A1 < 42 < ... < 46 > A7 > 48 > ...> A11, 
ou seja, está ordenado em ordem crescente até o sexto elemento,
e a partir desse elemento está ordenado em ordem decrescente. 
Dado o vetor da questão anterior, proponha um algoritmo para ordenar os elementos.
"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Ordem crescente', sorted(a)[0:6])
print('Ordem decrescente:', sorted(a, reverse=True)[0:4])
