# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

# Código Bard
def eh_primo(n):
  """Verifica se um número é primo."""
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True


def main():
  """Principais funções."""
  n = int(input("Digite o valor de N: "))
  contador = 0

  for i in range(2, n + 1):
    if eh_primo(i):
      print(i, end=" ")
      contador += 1

  print()
  print("O número de testes executados foi:", contador)


if __name__ == "__main__":
  main()
