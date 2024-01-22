# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
# Código Bard
"""import datetime

data = input("Digite uma data no formato dd/mm/aaaa: ")
try:
  datetime.datetime.strptime(data, "%d/%m/%Y")
  print(f"A data {data} é válida.")
except ValueError:
  print(f"A data {data} é inválida.")
"""

# Meu código
data = input('Digite uma data no formato dd/mm/aaaa: ')
data = data.split('/')
if len(data[0]) == 2 and len(data[1]) == 2 and len(data[2]) == 4:
    print('Data válida')
else:
    print('Data inválida')
