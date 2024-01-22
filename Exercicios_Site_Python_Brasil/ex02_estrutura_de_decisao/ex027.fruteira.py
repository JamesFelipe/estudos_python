"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
receberá ainda um desconto de 10% sobre este total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""
# Código bard
def calcular_valor_frutas(qtd_morangos, qtd_macas):
  """
  Calcula o valor a ser pago por frutas, conforme tabela de preços informada.

  Args:
    qtd_morangos: Quantidade de morangos em Kg.
    qtd_macas: Quantidade de maçãs em Kg.

  Returns:
    O valor a ser pago pelo cliente.
  """

  # Calcula o valor dos morangos
  valor_morangos = 0
  if qtd_morangos <= 5:
    valor_morangos = qtd_morangos * 2.5
  else:
    valor_morangos = qtd_morangos * 2.2

  # Calcula o valor das maçãs
  valor_macas = qtd_macas * 1.8

  # Calcula o valor total da compra
  valor_total = valor_morangos + valor_macas

  # Verifica se há desconto
  tem_desconto = (qtd_morangos + qtd_macas > 8) or (valor_total > 25)
  if tem_desconto:
    desconto = valor_total * 0.1
    valor_total -= desconto

  # Retorna o valor a ser pago
  return valor_total


if __name__ == "__main__":
  # Lê a quantidade de morangos
  qtd_morangos = float(input("Quantidade de morangos (Kg): "))

  # Lê a quantidade de maçãs
  qtd_macas = float(input("Quantidade de maçãs (Kg): "))

  # Calcula o valor a ser pago
  valor_pago = calcular_valor_frutas(qtd_morangos, qtd_macas)

  # Imprime o valor a ser pago
  print("Valor a ser pago: R$", valor_pago)
