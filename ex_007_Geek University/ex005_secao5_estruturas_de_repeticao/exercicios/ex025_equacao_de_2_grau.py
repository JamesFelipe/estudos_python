"""
Calcule as raízes da equação de 2º grau.
Lembrando que:

    x = -b +- √Δ / 2a 
    onde: Δ = B² - 4ac
    e ax² + bx + c = 0 representa uma equação de 2º grau.
A variável 'a' tem que ser diferente de zero. Caso seja igual, imprima a mensagem “Não
é equação de segundo grau”.

e Se Δ < 0, não existe real. Imprima a mensagem Não existe raiz.
e Se Δ = 0, existe uma raiz real. Imprima a raiz e a mensagem Raiz única.
e Se Δ >= 0 , imprima as duas raízes reais.
"""
# Código bard(modificado)
import math
# Entrada dos dados
a, b, c = input("Digite os coeficientes a, b e c da equação: ").split()
a = float(a)
b = float(b)
c = float(c)

# Verificação da equação de 2º grau
if a == 0:
  print("Não é equação de segundo grau")
  exit()

# Cálculo do discriminante
delta = b ** 2 - 4 * a * c

# Verificação do valor do discriminante
if delta < 0:
  print("Não existe raiz")
elif delta == 0:
  x = -b / 2 * a
  print("Raiz única:", x)
else:
  x1 = (-b + math.sqrt(delta)) / 2 * a
  x2 = (-b - math.sqrt(delta)) / 2 * a
  print("Raízes:", x1, x2)
