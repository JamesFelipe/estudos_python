# cotação do dolar dia 18 de julho de 2021 9:57 == 5,29
while True:
    try:
        real = float(input('Qauntos reais você quer converter R$: '))
         # cotação do dolar
        dolar = 5.29
    except ValueError:
        print('Apenas valores númericos serão aceitos...')
    else:  
        print(f'Com R$ {real} você tem US$ {real/dolar:.2f}')
        break
