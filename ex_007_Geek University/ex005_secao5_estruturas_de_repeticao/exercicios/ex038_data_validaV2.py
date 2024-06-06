"""
Leia uma data de nascimento de uma pessoa fornecida através de três números inteiros:
Dia, Mês e Ano. 

Teste a validade desta data para saber se esta é uma data válida. Teste
se o dia fornecido é um dia válido: dia > 0, dia < 28 para o mês de fevereiro (29 se o
ano for bissexto), dia < 30 em abril, junho, setembro e novembro, dia < 31 nos outros
meses. Teste a validade do mês: mês > 0 e mês < 13. Teste a validade do ano: ano <
ano atual (use uma constante definida com o valor igual a 2008). Imprimir: “data válida”
ou “data inválida” no final da execução do programa.
"""
# Código Bard

def eh_bissexto(ano):
  """
  Verifica se o ano é bissexto.

  Args:
    ano: ano a ser verificado.

  Returns:
    True se o ano é bissexto, False caso contrário.
  """

  return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

# Lê a data de nascimento

dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

# Verifica a validade do dia

if dia <= 0 or dia > 31:
  print("Dia inválido")
  exit()

# Verifica a validade do mês

if mes <= 0 or mes > 12:
  print("Mês inválido")
  exit()

# Verifica a validade do ano

if ano >= 2008:
  print("Ano inválido")
  exit()

# Verifica se o ano é bissexto

if mes == 2 and eh_bissexto(ano):
  limite = 29
else:
  limite = 28

# Verifica a validade do dia para o mês de fevereiro

if mes == 2 and dia > limite:
  print("Dia inválido")
  exit()

# Verifica a validade do dia para os meses de abril, junho, setembro e novembro

if mes in (4, 6, 9, 11) and dia > 30:
  print("Dia inválido")
  exit()

# Data válida

print("Data válida")
