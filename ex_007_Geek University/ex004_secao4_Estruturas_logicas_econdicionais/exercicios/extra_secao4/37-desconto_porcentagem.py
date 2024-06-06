while True:
    try:
        produto = float(input('Qual o valor do produto? '))
        # formula do desconto
        desconto = produto - (produto * 12/100) 
    except ValueError:
        print('Apenas valores númericos são aceitos...')
    else:
        print(f'O produto com 12% de desnconto sairá por {desconto}')   
        break
