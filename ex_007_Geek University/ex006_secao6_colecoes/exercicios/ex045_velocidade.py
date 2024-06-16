"""
Faça um algoritmo que converta uma velocidade expressa em km/h para m/s 
e vice versa. 
Você deve criar um menu com as duas opções de conversão e com uma opção para finalizar o programa. 

O usuário poderá fazer quantas conversões desejar, 
sendo que o programa só será finalizado quando a opção de finalizar for escolhida.
"""
import os
while True:
    menu = int(input("""
Menu de Opções:
1 - Converter Km/h para m/s
2 - Converter m/s para Km/h
3 - Sair do Programa
Digite aqui sua opção[Número]: """))
    match menu:
        case 1:
            velocidade = int(input("Digite o valor da velocidade: "))
            formula = velocidade / 3.6
            print(f'{velocidade} Km/h em m/s é: {formula:.2f}')
        case 2:
            velocidade = int(input("Digite o valor da velocidade: "))
            formula = velocidade * 3.6
            print(f'{velocidade} m/s em Km/h é: {formula:.2f}')
        case 3:
            print("Programa finalizado")
            break
        case _:
            os.system("cls")
            print("Essa opção é inválida, por favor tente outro valor")
            