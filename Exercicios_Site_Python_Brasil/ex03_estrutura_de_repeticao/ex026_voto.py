# Numa eleição existem três candidatos. 
# Faça um programa que peça o número total de eleitores. 
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
# código bard
def main():
  """Principais funções."""
  eleitores = int(input("Digite o número total de eleitores: "))
  votos = [0, 0, 0]  # vetor para armazenar os votos

  for i in range(eleitores):
    candidato = int(input("Digite o número do candidato: "))
    votos[candidato - 1] += 1

  print("Resultado da eleição:")
  for i in range(3):
    print("Candidato {}: {} votos".format(i + 1, votos[i]))


if __name__ == "__main__":
  main()
