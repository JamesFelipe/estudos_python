"""
Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido pro-
porcionalmente ao valor que cada deu para a realização da aposta. Faça um programa
que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um
ganharia do prêmio com base no valor investido.
"""

# Código Bard
def dividir_premio(valor_premio, valor_aposta_a, valor_aposta_b, valor_aposta_c):
  """
  Divide o prêmio da loteria proporcionalmente ao valor investido por cada apostador.

  Args:
    valor_premio: Valor do prêmio da loteria.
    valor_aposta_a: Valor da aposta do apostador A.
    valor_aposta_b: Valor da aposta do apostador B.
    valor_aposta_c: Valor da aposta do apostador C.

  Returns:
    Listas com o valor que cada apostador ganharia do prêmio.
  """

  # Calcula o total investido pelos apostadores.
  total_investido = valor_aposta_a + valor_aposta_b + valor_aposta_c

  # Calcula a porcentagem do prêmio que cada apostador ganharia.
  porcentagem_a = valor_aposta_a / total_investido
  porcentagem_b = valor_aposta_b / total_investido
  porcentagem_c = valor_aposta_c / total_investido

  # Calcula o valor que cada apostador ganharia do prêmio.
  valor_ganho_a = porcentagem_a * valor_premio
  valor_ganho_b = porcentagem_b * valor_premio
  valor_ganho_c = porcentagem_c * valor_premio

  # Retorna as listas com o valor que cada apostador ganharia do prêmio.
  return [valor_ganho_a, valor_ganho_b, valor_ganho_c]


# Lê o valor do prêmio e o valor investido por cada apostador.
valor_premio = float(input("Qual o valor do prêmio? "))
valor_aposta_a = float(input("Quanto investiu o apostador A? "))
valor_aposta_b = float(input("Quanto investiu o apostador B? "))
valor_aposta_c = float(input("Quanto investiu o apostador C? "))

# Divide o prêmio proporcionalmente ao valor investido.
valores_ganho = dividir_premio(valor_premio, valor_aposta_a, valor_aposta_b, valor_aposta_c)

# Imprime o valor que cada apostador ganharia do prêmio.
print("Apostador A: R$", valores_ganho[0])
print("Apostador B: R$", valores_ganho[1])
print("Apostador C: R$", valores_ganho[2])
