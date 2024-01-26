"""
Encontrar números primos é uma tarefa difícil.
Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
"""
# Código Bard
def eh_primo(n):
  """
  Retorna True se o número n é primo, False caso contrário.
  """
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True


def gerar_primos(n):
  """
  Gera uma lista dos números primos existentes entre 1 e n.
  """
  primos = []
  for i in range(2, n + 1):
    if eh_primo(i):
      primos.append(i)
  return primos


def main():
  n = int(input("Informe um número inteiro: "))
  primos = gerar_primos(n)
  print(f"Os números primos entre 1 e {n} são: {primos}")


if __name__ == "__main__":
  main()
