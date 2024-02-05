# Faça um programa, com uma função que dado uma lista e uma posição da mesma faça o quartil dessa posição
# p_index = int(p * len(lista))

# Código ChatGpt(modificado)
import numpy as np

def quartil_posicao(lista, p):
    # Ordenar a lista
    lista_ordenada = sorted(lista)
    
    # Calcular o índice correspondente ao quartil
    p_index = int(p * len(lista_ordenada))
    
    # Calcular o quartil na posição específica
    quartil = np.percentile(lista_ordenada, p * 100)
    
    return quartil

# Exemplo de uso
dados = [15, 22, 29, 31, 36, 40, 42, 51, 52, 57]
posicao_quartil_1 = 0.25  
posicao_quartil_2 = 0.50
posicao_quartil_3 = 0.75

resultado = quartil_posicao(dados, posicao_quartil_1)
resultado2 = quartil_posicao(dados, posicao_quartil_2)
resultado3 = quartil_posicao(dados, posicao_quartil_3)
print(f"O quartil na posição {posicao_quartil_1 * 100}% é: {resultado}")
print(f"O quartil na posição {posicao_quartil_2 * 100}% é: {resultado2}")
print(f"O quartil na posição {posicao_quartil_3 * 100}% é: {resultado3}")