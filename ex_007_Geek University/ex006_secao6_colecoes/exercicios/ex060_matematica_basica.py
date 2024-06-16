"""
Faça um programa que leia vários números, calcule e mostre:
(a) A soma dos números digitados
(b) A quantidade de números digitados 
(c) A média dos números digitados
(d) O maior número digitado 
(e) O menor número digitado
(f) A média dos números pares
Finalize a entrada de dados caso o usuário informe o valor 0.
"""
soma = contador = media = soma_pares = 0
maior = 0
menor = 99999
while True:
    numeros = int(input("Digite um valor inteiro[0 para sair]: "))
    if numeros == 0:
        break
    else:
        contador += 1
        soma += numeros
        media = soma / contador

    if numeros > maior:
        maior = numeros
    
    if numeros < menor:
        menor = numeros
        
    if numeros % 2 == 0:
        soma_pares += numeros
        
print(f"\nA soma dos números digitados é: {soma}")
print(f"Foram digitados {contador} números")
print(f'A média dos números digitados é: {media:.2f}')
print(f'A maior número digitado foi: {maior}')
print(f'O menor número digitado foi: {menor}')
print(f"A soma dos números pares digitados é: {soma_pares}")
