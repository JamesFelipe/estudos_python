km = float(input('Digite a quantidade de Quilometros percorridas: '))
litros = float(input('Digite a quantidade de litros consumidas: '))
consumo = km/ litros

if consumo < 8:
    print('Venda o Carro!')
elif consumo > 8 and consumo <= 14:
    print('Econômico!') 
elif consumo > 12:
    print('Super Econômico!')
