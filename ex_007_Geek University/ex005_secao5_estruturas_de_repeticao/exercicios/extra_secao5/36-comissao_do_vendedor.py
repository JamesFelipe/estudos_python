venda = float(input('Digite o valor da venda Mensal: '))

if venda >= 100_000:
    comissao = 700 + (venda * 0.16)  
    print(f'Comisão do vendedor: R${comissao:.2f}')
elif venda < 100_000 and venda >= 80_000:
   comissao = 650 + (venda * 0.14)
   print(f'Comisão do vendedor: R${comissao:.2f}')
elif venda < 80_000 and venda >= 60_000:
    comissao = 600 + (venda * 0.14)
    print(f'Comisão do vendedor: R${comissao:.2f}')
elif venda < 60_000 and venda >= 40_000:
    comissao = 550 + (venda * 0.14)
    print(f'Comisão do vendedor: R${comissao:.2f}')
elif venda < 40_000 and venda >= 20_000:
    comissao = 500 + (venda * 0.14)
    print(f'Comisão do vendedor: R${comissao:.2f}')
elif venda < 20_000:
    comissao = 400 + (venda * 0.14)
    print(f'Comisão do vendedor: R${comissao:.2f}')
