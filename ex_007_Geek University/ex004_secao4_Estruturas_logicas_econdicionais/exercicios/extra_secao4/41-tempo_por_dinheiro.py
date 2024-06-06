while True:
    try:
        hora_trabalho = float(input('Quanto você ganha por hora R$? '))
        trabalhado = float(input('Por quantas horas você trabalhou? '))
       
        #formulas
        mes = hora_trabalho * trabalhado
        porcentagem = mes + (mes * 10 / 100)
    except ValueError:
        print('Apenas valores númericos serão aceitos...')
    else:
        print(f'Você receberá pelo seu trabalho: R$ {porcentagem:.2f}')
        break
