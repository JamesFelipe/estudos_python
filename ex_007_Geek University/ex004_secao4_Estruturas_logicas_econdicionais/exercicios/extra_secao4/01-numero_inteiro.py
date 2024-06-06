# gerando o loop infinito para só sair se não tiver nenhum error
while True:
    # testando o código 
    try: 
        n = int(input('Digite um valor: '))  
    #valor do erro
    except ValueError: 
        print('Apenas números inteiros serão aceitos')
    # resultado se não tiver errros
    else: 
        print(f'Número digitado: {n}')
        break
