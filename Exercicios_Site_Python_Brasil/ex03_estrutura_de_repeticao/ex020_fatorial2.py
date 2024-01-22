# Altere o programa de cálculo do fatorial, 
# permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
# Código Bard
def fatorial(n):
  """Calcula o fatorial de um número inteiro."""
  if n < 0 or n > 15:
    raise ValueError("Número deve ser inteiro positivo e menor que 16.")
  if n == 0:
    return 1
  else:
    return n * fatorial(n - 1)


def main():
  """Permite ao usuário calcular o fatorial várias vezes."""
  while True:
    n = int(input("Digite um número inteiro: "))
    try:
      print(f"O fatorial de {n} é {fatorial(n)}.")
    except ValueError:
      print("Número inválido.")
    resposta = input("Deseja calcular o fatorial de outro número? (S/N): ").strip()
    if resposta != "S":
      break


if __name__ == "__main__":
  main()
