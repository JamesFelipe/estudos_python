# 29. Escreva um programa para calcular o valor da série, para 5 termos.
# S=0+1/2+2/4!+3/6!+...
e = 1
fatorial = 1
for i in range(1, 5):
    fatorial *= i
    e += 1 / fatorial
print(f"O valor de E é: {e:.2f}")
