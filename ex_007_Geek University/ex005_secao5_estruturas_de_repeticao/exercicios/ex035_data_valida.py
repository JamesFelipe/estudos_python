"""
Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12,
e se o dia existe naquele mês. Note que Fevereiro tem 29 dias em anos bissextos, e 28
dias em anos não bissextos.
"""

# Código Bard
def eh_data_valida(data):
  """
  Verifica se uma data é válida.

  Args:
    data: Uma string no formato "dd/mm/aaaa".

  Returns:
    True se a data é válida, False caso contrário.
  """

  dia, mes, ano = data.split("/")

  # Validar mês

  mes = int(mes)
  if mes < 1 or mes > 12:
    return False

  # Validar ano bissexto

  ano = int(ano)
  bissexto = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0

  # Validar dia

  dia = int(dia)
  if mes == 2:
    if bissexto:
      if dia < 1 or dia > 29:
        return False
    else:
      if dia < 1 or dia > 28:
        return False
  else:
    numero_dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if dia < 1 or dia > numero_dias_mes[mes - 1]:
      return False

  return True


data = input("Digite uma data no formato dd/mm/aaaa: ")

if eh_data_valida(data):
  print("Data válida.")
else:
  print("Data inválida.")
