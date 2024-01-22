"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A
ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
"""
# Código Bard
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
  # População inicial de A
  populacao_a = 80000
  # Taxa de crescimento anual de A
  taxa_crescimento_a = 3
  # População inicial de B
  populacao_b = 200000
  # Taxa de crescimento anual de B
  taxa_crescimento_b = 1.5

  # Anos necessários para que A ultrapasse ou iguale B
  anos = 0
  while populacao_a < populacao_b:
    populacao_a = crescimento_populacional(populacao_a, taxa_crescimento_a, anos)
    populacao_b = crescimento_populacional(populacao_b, taxa_crescimento_b, anos)
    anos += 1

  # Imprime o resultado
  print(f"Após {anos} anos, a população de A ultrapassará ou igualará a população de B.")


if __name__ == "__main__":
  main()
