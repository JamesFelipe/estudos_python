"""
Escreva o menu de opções abaixo. Loia a opção do usuário o oxecuto a oporação esco-
lhida, Escreva uma mensagem de erro se a opção for inválida.

Escolha a opção
1- Soma de 2 números
2- Diferença entre 2 números (maior pelo menor)
3- Produtp entre 2 números
4- Divisão entre 2 núneros (o denominador não pode ser zero).

Opção
"""
opcao = int(input('''
Escolha a opção

1 - Soma de 2 números
2 - Diferença entre 2 números
3 - Produto entre 2 números
4 - Divisão entre 2 números

Opção[Número]: '''))
match opcao:
    case 1:
        numero1 = int(input('Digite o primeiro valor inteiro: '))
        numero2 = int(input('Digite o segundo valor inteiro: '))
        print(f'{numero1} + {numero2} = {numero1 + numero2}')
    case 2:
        numero1 = int(input('Digite o primeiro valor inteiro: '))
        numero2 = int(input('Digite o segundo valor inteiro: '))
        if numero1 > numero2:
            print(f'{numero1} - {numero2} = {numero1 - numero2}')
        elif numero2 > numero1:
            print(f'{numero2} - {numero1} = {numero2 - numero1}')
    case 3:
        numero1 = int(input('Digite o primeiro valor inteiro: '))
        numero2 = int(input('Digite o segundo valor inteiro: '))
        print(f'{numero1} X {numero2} = {numero1 * numero2}')
    case 4:
        numero1 = int(input('Digite o primeiro valor inteiro: '))
        numero2 = int(input('Digite o segundo valor inteiro: '))
        if numero1 == 0 or numero2 == 0:
            print(f'Não posso dividir valores por zero. Programa Encerrado....')
        else:
            if numero1 > numero2:
                print(f'{numero1} / {numero2} = {numero1 / numero2}')
            elif numero2 > numero1:
                print(f'{numero2} / {numero1} = {numero2 / numero1}')
    case _:
        print('Valor inválido')
