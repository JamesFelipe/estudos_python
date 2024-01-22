"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
porém não há limites para a quantidade de carne por cliente. 
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 

Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""
# Código bard
def gerar_cupom_fiscal(tipo_carne, qtd_carne, forma_pagamento):
  """
  Gera um cupom fiscal de carnes, conforme tabela de preços informada.

  Args:
    tipo_carne: Tipo de carne comprada.
    qtd_carne: Quantidade de carne comprada, em Kg.
    forma_pagamento: Forma de pagamento.

  Returns:
    O cupom fiscal gerado.
  """

  # Verifica o tipo de carne
  if tipo_carne == "File Duplo":
    preco_kg = 4.90
  elif tipo_carne == "Alcatra":
    preco_kg = 5.90
  elif tipo_carne == "Picanha":
    preco_kg = 6.90
  else:
    raise ValueError("Tipo de carne inválido.")

  # Verifica a quantidade de carne
  if qtd_carne <= 5:
    preco_total = qtd_carne * preco_kg
  else:
    preco_total = qtd_carne * preco_kg * 1.1

  # Verifica a forma de pagamento
  if forma_pagamento == "Cartão Tabajara":
    desconto = preco_total * 0.05
    preco_total -= desconto

  # Gera o cupom fiscal
  cupom = """
  **Cupom Fiscal**

  Tipo de carne: {}
  Quantidade: {} Kg
  Preço total: R$ {:.2f}
  Forma de pagamento: {}
  Valor do desconto: R$ {:.2f}
  Valor a pagar: R$ {:.2f}
  """.format(tipo_carne, qtd_carne, preco_total, forma_pagamento, desconto, preco_total - desconto)

  return cupom


if __name__ == "__main__":
  # Lê o tipo de carne
  tipo_carne = input("Tipo de carne: ")

  # Lê a quantidade de carne
  qtd_carne = float(input("Quantidade de carne (Kg): "))

  # Lê a forma de pagamento
  forma_pagamento = input("Forma de pagamento: ")

  # Gera o cupom fiscal
  cupom = gerar_cupom_fiscal(tipo_carne, qtd_carne, forma_pagamento)

  # Imprime o cupom fiscal
  print(cupom)
