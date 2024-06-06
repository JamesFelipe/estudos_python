print('''Menu de opções
1- Soma de 2 números
2 - Diferença entre 2 números (maior pelo menor)
3- Produto entre 2 números
4- Divisão entre 2 números (o denominador não pode por zero)
''')
op = int(input('Qual opção você quer? (valor númerico): '))
if op == 1:
    n1 = int(input('Digite um valor inteiro: '))
    n2 = int(input('Digite o mesmo/outro valor inteiro: '))
    print(f'{n1} + {n2} = {n1 + n2}')
elif op == 2:
    n1 = int(input('Digite o valor maior: '))
    n2 = int(input('Digite o valor menor: '))
    print(f'{n1} - {n2} = {n1 - n2}')
elif op == 3:
    n1 = int(input('Digite um valor inteiro: '))
    n2 = int(input('Digite o mesmo/outro valor inteiro: '))
    print(f'{n1} X {n2} = {n1 * n2}')
elif op == 4:
    n1 = int(input('Digite um valor inteiro: '))
    if n1 == 0:
        print('Não existe divisão por zero')
    else:
        n2 = int(input('Digite o mesmo/outro valor inteiro: '))
        if n2 == 0:
            print('Não existe zero na divisão')
        else:
            print(f'{n1} / {n2} = {n1 / n2}')
else:
    print('Valor inexistente...')
