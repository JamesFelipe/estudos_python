"""
Faça um programa que some os números impares contidos em um intervalo definido pelo usuário. 
O usuário define o valor inicial do intervalo e o valor final deste intervalo
e o programa deve somar todos os números ímpares contidos neste intervalo. 
Caso o usuário digite um intervalo inválido (começando por um valor maior que o valor final) 
deve ser escrito uma mensagem de erro na tela, "Intervalo de valores inválido" 
e o programa termina. Exemplo de tela de saída: Digite o valor inicial e valor final: 5
10
Soma dos ímpares neste intervalo: 21

"""
soma_impares = 0
valor_inicial = int(input("Digite qual o valor inicial do intervalo: "))
valor_final = int(input("Digite qual o valor final do intervalo: "))
if valor_inicial >= valor_final:
    print("Intervalo de valores inválidos")
else:
    for i in range(valor_inicial, valor_final + 1):
        if i % 2 == 1:
            soma_impares += i
print(f"Soma dos ímpares neste intervalor: {soma_impares}")
