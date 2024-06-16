maior = cont = 0
numero = int(input("Digite quantos números você quer digitar: "))
for i in range(1, numero + 1):
    numeros = int(input(f"Digite o {i}º valor inteiro: "))
    if numeros > maior:
        maior = numeros
    if numeros == maior:
        cont += 1   
    
print(f"O maior número digitado foi: {maior}, e ele apareceu {cont} vezes")
