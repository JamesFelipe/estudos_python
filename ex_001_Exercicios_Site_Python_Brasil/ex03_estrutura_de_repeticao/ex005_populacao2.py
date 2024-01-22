# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
# Código Bard(modificado)
import re

def crescimento_populacional(populacao, taxa_crescimento, anos):
  """
  Calcula o crescimento populacional de uma população inicial, com uma taxa de crescimento anual, ao longo de um número de anos.

  Args:
    populacao: População inicial.
    taxa_crescimento: Taxa de crescimento anual, em porcentagem.
    anos: Número de anos.

  Returns:
    População após o crescimento.
  """

  crescimento = populacao * (1 + taxa_crescimento / 100) ** anos
  return crescimento


def main():
  # Valida a entrada
  while True:
    populacao_a = input("Informe a população inicial de A: ")
    if not populacao_a.isdigit():
      print("A população inicial deve ser um número inteiro.")
      continue
    populacao_a = int(populacao_a)

    taxa_crescimento_a = input("Informe a taxa de crescimento anual de A: ")
    if not taxa_crescimento_a.isdigit():
      print("A taxa de crescimento deve ser um número inteiro.")
      continue
    taxa_crescimento_a = int(taxa_crescimento_a)

    populacao_b = input("Informe a população inicial de B: ")
    if not populacao_b.isdigit():
      print("A população inicial deve ser um número inteiro.")
      continue
    populacao_b = int(populacao_b)

    taxa_crescimento_b = input("Informe a taxa de crescimento anual de B: ")
    if not taxa_crescimento_b.isdigit():
      print("A taxa de crescimento deve ser um número inteiro.")
      continue
    taxa_crescimento_b = int(taxa_crescimento_b)

    break

  # Anos necessários para que A ultrapasse ou iguale B
  anos = 0
  while populacao_a < populacao_b:
    populacao_a = crescimento_populacional(populacao_a, taxa_crescimento_a, anos)
    populacao_b = crescimento_populacional(populacao_b, taxa_crescimento_b, anos)
    anos += 1

  # Imprime o resultado
  print(f"Após {anos} anos, a população de A ultrapassará ou igualará a população de B.")

  # Permite repetir a operação
  resposta = input("Deseja repetir a operação? (S/N): ")
  if resposta.upper() == "S":
    main()


if __name__ == "__main__":
  main()
