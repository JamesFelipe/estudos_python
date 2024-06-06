while True:
    try:
        sal = float(input('Digite seu salário R$: '))
      
        # formulas
        bonus = sal + (sal * 5/100)
        imposto = bonus - (bonus * 7/100)
    except ValueError:
        print('Apenas valores númericos serão aceitos...')
    else:
        print(f'Com 5% de bônus e 7% de imposto você irá receber: R$ {imposto}')
        break
2