"""
Faça um programa para ler as dimensões de um terreno (comprimento c e largura l),
bem como o preço do metro de tela p. Imprima o custo para cercar este mesmo terreno
com tela.
"""

# Código Bard

def calcular_custo_cerca(comprimento, largura, preco_metro):
  """
  Calcula o custo para cercar um terreno com tela.

  Args:
    comprimento: Comprimento do terreno.
    largura: Largura do terreno.
    preco_metro: Preço do metro de tela.

  Returns:
    O custo para cercar o terreno.
  """

  # Calcula o perímetro do terreno.
  perimetro = 2 * (comprimento + largura)

  # Calcula a quantidade de tela necessária.
  quantidade_tela = perimetro / 100

  # Calcula o custo total da tela.
  custo_total = quantidade_tela * preco_metro

  return custo_total


# Lê as dimensões do terreno e o preço do metro de tela.
comprimento = float(input("Qual o comprimento do terreno? "))
largura = float(input("Qual a largura do terreno? "))
preco_metro = float(input("Qual o preço do metro de tela? "))

# Calcula o custo para cercar o terreno.
custo_cerca = calcular_custo_cerca(comprimento, largura, preco_metro)

# Imprime o custo para cercar o terreno.
print("O custo para cercar o terreno é de R$", custo_cerca)
