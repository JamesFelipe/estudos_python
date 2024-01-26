"""
Uma academia deseja fazer um senso entre seus clientes  X
para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, X
para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código,
sua altura e seu peso.  X
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. X
Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto,
do mais baixo, do mais gordo e do mais magro, 
além da média das alturas e dos pesos dos clientes X
"""
# Código Bard
def eh_valido(codigo):
  """
  Retorna True se o código é válido, False caso contrário.
  """
  return codigo >= 0 and codigo <= 99999


def main():
  clientes = []
  altura_maxima = -1
  altura_minima = 999999
  peso_maximo = -1
  peso_minimo = 999999
  media_altura = 0
  media_peso = 0

  while True:
    codigo = int(input("Informe o código do cliente: "))
    if not eh_valido(codigo):
      print("Código inválido.")
      continue

    altura = float(input("Informe a altura do cliente (em metros): "))
    peso = float(input("Informe o peso do cliente (em kg): "))

    clientes.append((codigo, altura, peso))

    if altura > altura_maxima:
      altura_maxima = altura
      cliente_alto = clientes[-1]

    if altura < altura_minima:
      altura_minima = altura
      cliente_baixo = clientes[-1]

    if peso > peso_maximo:
      peso_maximo = peso
      cliente_gordo = clientes[-1]

    if peso < peso_minimo:
      peso_minimo = peso
      cliente_magro = clientes[-1]

    media_altura += altura
    media_peso += peso

    if codigo == 0:
      break

  media_altura /= len(clientes)
  media_peso /= len(clientes)

  print("Resultados do senso:")
  print("Cliente mais alto:", cliente_alto)
  print("Cliente mais baixo:", cliente_baixo)
  print("Cliente mais gordo:", cliente_gordo)
  print("Cliente mais magro:", cliente_magro)
  print("Média de altura:", media_altura)
  print("Média de peso:", media_peso)


if __name__ == "__main__":
  main()