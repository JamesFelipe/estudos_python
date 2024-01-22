"""
Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""
import math
# Código Bard
# Declaração de variáveis
area = float()
litros = float()
latas = float()
galoes = float()
custo_latas = float()
custo_galoes = float()
custo_total = float()

# Entrada de dados
print("Qual é o tamanho da área a ser pintada (em metros quadrados)?")
area = float(input())

# Cálculo da quantidade de tinta necessária
litros = area / 6
litros = litros * 1.1  # Adicionando 10% de folga

# Cálculo da quantidade de latas necessárias
latas = litros / 18
latas = math.ceil(latas)  # Arredondando para cima

# Cálculo da quantidade de galões necessários
galoes = litros / 3.6
galoes = math.ceil(galoes)  # Arredondando para cima

# Cálculo do custo das latas
custo_latas = latas * 80

# Cálculo do custo dos galões
custo_galoes = galoes * 25

# Cálculo do custo total
custo_total = custo_latas + custo_galoes

# Impressão dos resultados
print("Quantidade de latas necessárias:", latas)
print("Quantidade de galões necessários:", galoes)
print("Custo das latas: R$", custo_latas)
print("Custo dos galões: R$", custo_galoes)
print("Custo total: R$", custo_total)
