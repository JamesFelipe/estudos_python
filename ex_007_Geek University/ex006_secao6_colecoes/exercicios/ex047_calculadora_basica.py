"""
Faça um programa que apresente um menu de opções
para o cálculo das seguintes operações entre dois números:
    - adição (opção 1)
    - subtração (opção 2)
    - multiplicação (opção 3)
    - divisão (opção 4).
    - saída (opção 5)
    
O programa deve possibilitar ao usuário a escolha da operação desejada, 
a exibição do resultado e a volta ao menu de opções. 
O programa só termina quando for escolhida a opção de saída (opção 5).
"""

while True:
    opcao = int(input("""
===== Menu de Opções =====
[ 1 ] - Adição
[ 2 ] - Subtração
[ 3 ] - Multiplicação
[ 4 ] - Divisão
[ 5 ] - Sair do Programa

Digite aqui sua opção[Número]: """))
    match opcao:
        case 1:
            numero1 = int(input("Digite um número inteiro: "))
            numero2 = int(input("Digite o mesmo/outro número inteiro: "))
            print(f"{numero1} + {numero2} = {numero1 + numero2}")
        case 2:
            numero1 = int(input("Digite um número inteiro: "))
            numero2 = int(input("Digite o mesmo/outro número inteiro: "))
            print(f"{numero1} - {numero2} = {numero1 - numero2}")
        case 3:
            numero1 = int(input("Digite um número inteiro: "))
            numero2 = int(input("Digite o mesmo/outro número inteiro: "))
            print(f"{numero1} X {numero2} = {numero1 * numero2}")
        case 4:
            numero1 = int(input("Digite um número inteiro: "))
            numero2 = int(input("Digite o mesmo/outro número inteiro: "))
            if numero2 == 0:
                print("Não é possível dividir por zero, tente outros valores...")
            else:
                print(f"{numero1} / {numero2} = {numero1 / numero2}")
        case 5:
            print("Programa finalizado")
            break
        case _:
            print("Opção inválida, Escolha outra opção...")
