# Faca um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número dado
# Código ChatGpt modificado
numero = int(input("Digite um número inteiro: "))
print("O primeiro multiplo é: ")
for i in range(1, numero):
    i = numero + 1
    if (i % 11 == 0 or i % 13 == 0 or i % 17 == 0):
        i += 1
print(i)
