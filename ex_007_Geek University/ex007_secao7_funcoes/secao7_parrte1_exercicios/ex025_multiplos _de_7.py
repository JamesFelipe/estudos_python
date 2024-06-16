"""
Faça um programa que preencha um vetor de tamanho 100 com os 100 primeiros 
naturais que não são múltiplos de 7 ou que terminam com 7.
"""
vetor = [x for x in range(1, 101) if x % 7 != 0 and str(x)[-1] == '7']
print(vetor)
