cont_pares = cont_numeros = numero = 0
while numero != 1000:
    numero = int(input("Digite um valor inteiro[1000 para sair]: "))
    cont_numeros += 1
    if numero % 2 == 0:
        cont_pares += 1
print(f"Foram lidos: {cont_numeros - 1} números")
print(f"Foram digitados: {cont_pares - 1} números pares")
