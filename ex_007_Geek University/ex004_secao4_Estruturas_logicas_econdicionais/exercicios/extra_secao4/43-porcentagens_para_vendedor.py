while True:
    try:
        valor_liquido = float(input('Digite o valor: '))
        desconto_dez = valor_liquido - (valor_liquido * 10 / 100)
    except ValueError:
        print('Apenas valores númericos serão aceitos...')
    else:
        print(f'Com 10% de desocnto você receberá {desconto_dez}')

        print(f'Em três vezes sem juros você pagará: {valor_liquido / 3:.2f}')

        # comissão de 5%
        comisao_a_vista = desconto_dez * 0.05 
        print(f'Comissão do vendedor a vista: R$ {comisao_a_vista}')

        comissao_parcelada = valor_liquido * 0.05
        print(f'Comissão do vendedor da venda parcelada: R$ {comissao_parcelada}')
        break
